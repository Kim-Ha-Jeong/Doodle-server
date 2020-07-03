from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Review(models.Model):
    image = models.ImageField()
    description = models.TextField()
    star = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'


class Produce(models.Model):
    doodle = models.ImageField()
    redesign = models.IntegerField()
    receiver = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=20)
    post_code = models.CharField(max_length=100)
    base_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)


