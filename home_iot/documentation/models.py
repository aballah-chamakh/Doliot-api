from django.db import models
from account.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from Shared.utils import unique_slug_generator

class Documentation(models.Model):
     title = models.CharField(max_length=500,blank=True, null=True)
     image = models.ImageField(default='iot.png')
     slug  = models.SlugField(blank=True,null=True)
     breif = models.TextField(blank=True, null=True)
     description = RichTextUploadingField(blank=True, null=True)
     likes   = models.ManyToManyField(User,blank=True,related_name='documentation_likes')
     published = models.BooleanField(default=False)

     def __str__(self):
         return 'the title of doc is '+self.title


@receiver(pre_save,sender=Documentation)
def set_documentation_slug(sender, instance, **kwargs):
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)
