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
    doodle = models.ImageField(null=True)
    redesign = models.IntegerField()
    amount = models.IntegerField()
    receiver = models.CharField(max_length=20)
    r_phone_num = models.CharField(max_length=20)
    post_code = models.CharField(max_length=100)
    base_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    order = models.CharField(max_length=20)
    o_phone_num = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
