from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Author(models.Model):
  name =  models.CharField(max_length=30)
  def __str__(self):
    return self.name


class Book(models.Model):
 title=models.CharField(max_length= 50)
 author=models.ForeignKey (Author , on_delete=models.CASCADE , related_name = 'author')
 def __str__(self):
     return self.title
 
class Library(models.Model):
  name= models.CharField(max_length= 30)
  books= models.ManyToManyField(Book)
  def __str__(self):
      return self.name
  

class Librarian(models.Model):
 name= models.CharField(max_length=30)
 library= models.OneToOneField (Library, on_delete=models.CASCADE , related_name = 'library')
 def __str__(self):
   return self.name
 



class UserProfile(models.Model):
  user = models.OneToOneField(User , on_delete=models.CASCADE)
  role = models.CharField(max_length=20, choices=[('Admin','Admin'),('Librarian','Librarian'),('Member','Member')])
  def __str__(self):
   return self.user

def CreatUserProfile(sender, instance, created, **kwargs ):
  

