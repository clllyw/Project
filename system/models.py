from django.db import models

# Create your models here.
#photo=models.ImageField(upload_to=settings.MEDIA_ROOT)
class Teacher(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Research_area = models.CharField(max_length=100)
    Email = models.EmailField()    
    Introduction = models.CharField(max_length=3000)
    Information = models.CharField(max_length=3000)
class Student(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30,default=False)
    Number = models.CharField(max_length=30)
    Institute = models.CharField(max_length=100)
    Contact_way = models.CharField(max_length=100)
    Email = models.EmailField()
    Myrequestteacher=models.CharField(max_length=50)
    Myrequestdate=models.CharField(max_length=50)
class User(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
class Usert(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
