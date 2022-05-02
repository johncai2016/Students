from django.db import models

# Create your models here.
class Family(models.Model):
  unique_id = models.CharField(max_length=32)
  student_name = models.CharField(max_length=32)
  family_name = models.CharField(max_length=32)
  inspection_time = models.DateTimeField()
  inspection_result =  models.CharField(max_length=32)
  
  
class Routing(models.Model):
  unique_id = models.CharField(max_length=32)
  student_name = models.CharField(max_length=32)
  phone = models.CharField(max_length = 11)
  has_star = models.BooleanField()
  show_time = models.DateTimeField()
