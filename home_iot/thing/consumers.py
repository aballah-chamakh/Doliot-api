from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from thing.models import Robot,Bulb,Plant
import json
# profile<id>__robot<id>
# ws//example.com/robot/id/?token=knlfjnqsllf

class RobotConsumer(AsyncJsonWebsocketConsumer) :
    async def websocket_connect(self,event):
        robot_id = self.scope['url_route']['kwargs']['pk']
        user_id = self.scope['user'].id
        username = self.scope['user'].username
        robot_name = await self.get_robot_name(robot_id)
        self.group_name = username.replace(' ','')+str(user_id)+'_'+robot_name.replace(' ','')+str(robot_id)
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def websocket_receive(self,event):

        direction = json.loads(event['text'])['direction']
        await self.channel_layer.group_send(self.group_name,{'type':'move.robot','direction':direction})


    async def websocket_disconnect(self,event):
        print(event)

    async def move_robot(self,event):
        print('moving robot to '+event['direction'])
        data = {'direction':event['direction']}
        await self.send_json(content=data)

    @database_sync_to_async
    def get_robot_name(self,robot_id):
        robot = Robot.objects.get(id=robot_id)
        return robot.name

class BulbConsumer(AsyncJsonWebsocketConsumer):

    async def websocket_connect(self,event):
        username = self.scope['user'].username
        user_id = self.scope['user'].id
        bulb_id = self.scope['url_route']['kwargs']['pk']
        bulb_name = await self.get_bulb_name(bulb_id)
        self.group_name = username.replace(' ','')+str(user_id)+'_'+bulb_name.replace(' ','')+str(bulb_id)
        print(self.group_name)
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def websocket_receive(self,event):
        action = json.loads(event['text'])['action']
        await self.toogle_bulb_db(action)
        await self.channel_layer.group_send(self.group_name,{'type':'toogle.bulb','action':action})

    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)

    async def toogle_bulb(self,event):
        data ={'state':event['action']}
        await self.send_json(content=data)

    @database_sync_to_async
    def get_bulb_name(self,bulb_id):
        self.bulb_obj = Bulb.objects.get(id=bulb_id)
        return self.bulb_obj.name

    @database_sync_to_async
    def toogle_bulb_db(self,action):
        state = None
        if action == 'on' :
            state = True
        elif action == 'off' :
            state = False
        self.bulb_obj.state = state
        self.bulb_obj.save()


class PlantConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self,event):
        plant_id = self.scope['url_rourte']['kawrgs']['id']
        self.plant_obj = await self.get_plant_obj(plant_id)
        plant_name = self.plant_obj.name
        username = self.scope['user'].username
        user_id = self.scope['user'].id
        self.group_name = username.replace(' ','')+user_id+'_'+plant_name.replace(' ','')+plant_id
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
    async def websocket_receive(self,event):
        data = json.loads(event['text'])
        type = data['type']
        if type == 'loging' :
            humidity_value = data['humidity_value']
            await self.set_plant_humidity_value(humidity_value)
        elif type == 'toogle' :
            action = data['action']
            await self.toogle_plant_db(action)
            self.channel_layer.group_send(self.group_name,{'type':'toogle.plant','action':action})

    async def toogle_plant(self,event):
        self.send_json(content={'action':event['action']})

    @database_sync_to_async
    def get_plant_name(self,plant_id):
        plant = Plant.object.get(id=plant_id)
        return plant.username
    @database_sync_to_async
    def set_plant_humidity_value(self,value):
        self.plant_obj.humidity = value
        self.plant.save()
    @database_sync_to_async
    def toogle_plant_db(self):
        if action == 'open':
            self.plant.opened = True
        else :
            self.plant.opened = False
        self.plant.save()
