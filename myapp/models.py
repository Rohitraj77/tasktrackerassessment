from django.db import models

# Create your models here.
class taskmanager(models.Model):
	title=models.CharField(max_length=90)
	description=models.CharField(max_length=200)
	email=models.EmailField()
	place=models.CharField(max_length=90)
	duedate=models.DateField()
	status=models.CharField(max_length=90)