from django.db import models

# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=10, unique=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
