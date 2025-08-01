from django.db import models

# Create your models here.

class Author(models.Model):
  name =  models.CharField(max_length=30)

class Book(models.Mode):
 title=models.CharField(max_length= 50)
 author=models.ForeignKey (Author , on_delete=models.CASCADE)

class Library(models.Model):
  name= models.CharField(max_length= 30)
  books= models.ManyToManyField(Book, on_delete=models.CASCADE)


class Librarian(models.Model):
 name= models.CharField(max_length=30)
 library= models.OneToOneField (Library, on_delete=models.CASCADE)