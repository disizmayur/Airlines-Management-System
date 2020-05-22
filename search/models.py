from django.db import models

# Create your models her
class search(models.Model):
    To=models.CharField(max_length=100)
    From=models.CharField(max_length=100)
    Date=models.DateField()
    Adult=models.IntegerField()
    Child=models.IntegerField()