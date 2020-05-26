from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()