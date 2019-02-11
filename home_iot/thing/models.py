from django.db import models

from account.models import Profile


from django.contrib.auth.models import User

# Create your models here.


class Bulb(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    on_image = models.ImageField(default='bulbOn.jpg')
    off_image = models.ImageField(default='bulbOff.jpg')
    name = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    def __str__(self):
        return 'the bulb '+self.name+' owned by '+self.profile.user.username

    @property
    def owner(self):
        return self.profile.user


class Robot(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(default='robot.png')
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    def __str__(self):
        return 'the robot '+self.name+' owned by '+self.profile.user.username

class Plant(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(default='plant.jpg')
    humidity = models.CharField(max_length=10,blank=True,null=True)
    opened = models.BooleanField(default=False)
    def __str__(self):
        return 'the plant '+self.name+' owned by '+self.profile.user.username
