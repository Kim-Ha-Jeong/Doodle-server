from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Photo(models.Model):
    doodle = models.ImageField()


class UserManager(BaseUserManager):
    user_in_migrations = True

    def _create_user(self, name, email, tel, photo_id, password=None):
        if not tel:
            raise ValueError('연락처를 입력해주세요')
        if not name:
            raise ValueError('이름을 입력해주세요')
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            tel=tel,
            photo_id=photo_id
        )
        user.save(using=self._db)
        return user

    def create_admin(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    tel = models.CharField(max_length=30)
    photo_id = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['id', ]

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
