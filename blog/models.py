from django.conf import settings
from django.db import models
from django.utils import timezone
import os
# Create your models here.
class Post(models.Model):	
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #upload = models.ImageField(upload_to ='media/') 
    #profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    #Main_Img = models.ImageField(upload_to='images/') 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
