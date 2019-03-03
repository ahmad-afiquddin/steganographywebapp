from django.db import models

# Create your models here.

class Steganography(models.Model):
	carrier = models.ImageField(upload_to="gallery", default="")
	payload = models.ImageField(upload_to="gallery", default="")
	retImg = models.ImageField(upload_to="gallery", default="")

