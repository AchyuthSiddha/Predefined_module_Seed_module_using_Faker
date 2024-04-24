from django.db import models

# Create your models here.


class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    smarks=models.IntegerField
    sdob=models.DateField()
    semail=models.EmailField()
    saddr=models.TextField()
    sphone=models.CharField(max_length=30)