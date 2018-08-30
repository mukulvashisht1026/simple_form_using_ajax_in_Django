from django.db import models

# Create your models here.
class tableModel(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	DOB = models.DateTimeField()
	updated = models.DateTimeField(auto_now_add= True)