from django.db import models
from django.core.validators import MinValueValidator


class Person(models.Model):
	GEN = {'male':'male','female':'female','other':'other'}
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=30,choices=GEN)
	address = models.TextField()
	city = models.CharField(max_length=30)
	contact_no = models.BigIntegerField()
	aadhar_card_no = models.BigIntegerField()
	email = models.EmailField()











