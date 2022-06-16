from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# the signal will help to update profile everytime a new user is added, so we don't need to 
# add it manually

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
  if created:
    print(sender)
    print(instance)
    print(created)
    Profile.objects.create(user=instance)
