from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Post(models.Model):
 title = models.CharField(max_length=200)
 content= models.TextField()
 published_date= models.DateTimeField(auto_now_add=True)
 author= models.ForeignKey (User, on_delete= models.CASCADE)



class Comment(models.Model):
 post = models.ForeignKey(Post , on_delete=models.CASCADE ,related_name= "comments")   #ForeignKey linking to the Post model, establishing#many-to-one relationship.
 author = models.ForeignKey(User , on_delete= models.CASCADE , related_name= "comments")                 #ForeignKey to Django’s User model, indicating the user who wrote the comment.
 content = models.TextField()                  #TextField for the comment’s text.
 created_at = models.DateTimeField(auto_now_add=True)               #DateTimeField that records the time the comment was made.
 updated_at = models.DateTimeField (auto_now=True)             #DateTimeField that records the last time the comment was updated.

