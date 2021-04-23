from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    CNIC = models.CharField(max_length=15,default='',null=True)
    contact = models.CharField(max_length=15,null=True,default='')
    address = models.TextField(default='',null=True)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,**kwargs):
        super().save()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()