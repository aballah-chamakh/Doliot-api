from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Lamp(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    def __str__(self):
        return 'the lamp "'+self.name+'" owned by '+self.owner.username


class Button(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    def __str__(self):
        return 'the button "'+self.name+'" owned by '+self.owner.username
