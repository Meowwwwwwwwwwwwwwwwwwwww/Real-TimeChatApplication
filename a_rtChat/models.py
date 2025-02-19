from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatGroup(models.Model):
    group_name= models.CharField(max_length= 128,unique= True)

# : The __str__ method defines how an instance of this model is displayed as a string. This is helpful when working with objects in the Django admin interface or the Python shell.
#For example, if you query a ChatGroup object, instead of displaying something like <ChatGroup object (1)>, it will display the group name (e.g., "Study Group")

    def __str__(self):
        return self.group_name

 
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name= 'chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body= models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    class Meta:
        ordering = ['-created_at']


