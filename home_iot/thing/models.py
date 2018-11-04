from django.db import models
from account.models import Profile


class Thing(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    on_image = models.ImageField(default='bulbOn.jpg')
    off_image = models.ImageField(default='bulbOff.jpg')
    name = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    def __str__(self):
        return 'the bulb "'+self.name+'" owned by '+self.profile.user.username

    @property
    def owner(self):
        return self.profile.user
