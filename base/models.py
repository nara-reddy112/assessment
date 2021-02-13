from django.db import models

# Create your models here.
class User(models.Model):
	id = models.CharField(max_length = 150, primary_key = True)
	real_name = models.CharField(max_length = 150)
	tz = models.CharField(max_length = 150)

class Activities(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	# activate = models.JSONField()
	start_time = models.CharField(max_length = 150)
	end_time = models.CharField(max_length = 150)