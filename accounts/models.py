from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Profile(models.Model):  # inherit
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # oneway deletion
    bio = models.TextField(max_length=300, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Mess(models.Model):
    
    name = models.CharField(max_length=20, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name



