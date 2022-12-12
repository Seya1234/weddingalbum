from django.db import models


# Create your models here.
class Engagement(models.Model):
    e_img = models.ImageField(upload_to='gallery')

class Mk_sreya(models.Model):
    mk_sreya_img = models.ImageField(upload_to='gallery')

class Mk_sethu(models.Model):
    mk_sethu_img = models.ImageField(upload_to='gallery')

class Wedding(models.Model):
    wedding_img = models.ImageField(upload_to='gallery')