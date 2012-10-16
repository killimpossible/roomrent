from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
	room_topic = models.CharField(max_length = 60)
	room_desc = models.TextField()
	house_type = models.CharField(max_length = 8)
	square = models.IntegerField()
	rent = models.IntegerField()
	pay_type = models.CharField(max_length = 20)
	pub_man = models.ForeignKey(User)
	pub_date = models.DateField()
	room_city = models.CharField(max_length = 20)
	room_address = models.CharField(max_length = 100)
	room_type = models.CharField(max_length = 40)
	facilities = models.CharField(max_length = 100)


