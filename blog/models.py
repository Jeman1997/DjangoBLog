from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    #Datetime options: 'auto_now':-update the date every time thers a update
                        #'auto_now_add':-add date created
                        #default:-can edit the time
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
