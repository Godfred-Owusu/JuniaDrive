from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Folder(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')
    
    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='user_files/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField()  # Track file size for storage limit

    def __str__(self):
        return self.name
    

    
# Signal to create default folders

# @receiver(post_save, sender=User)
# def create_default_folders(sender, instance, created, **kwargs):
#     if created:
#         Folder.objects.create(name='Documents', user=instance)
#         Folder.objects.create(name='Images', user=instance)
#         Folder.objects.create(name='Videos', user=instance)


@receiver(post_save, sender=User)
def create_default_folders(sender, instance, created, **kwargs):
    if created:
        print("Creating default folders for new user:", instance.username)
        Folder.objects.create(name='Documents', user=instance)
        Folder.objects.create(name='Images', user=instance)
        Folder.objects.create(name='Videos', user=instance)
        print("Default folders created")
