from random import randint

from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# class MyUser(AbstractUser):
#     image_field = ...
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Chipta(models.Model):
    raqam = models.IntegerField(null=False, unique=True)
    kompaniya = models.CharField(max_length=200, null=False, blank=False)
    ketish_vaqti = models.DateTimeField()
    kelish_vaqti = models.DateTimeField()
    qaysi_shaharga = models.CharField(max_length=200)
    qaysi_shahardan = models.CharField(max_length=200)
    soni = models.IntegerField()

    class Meta:
        verbose_name_plural = "Chiptalar"

    def __str__(self):
        return f"{self.raqam}"


class Yolovchi(models.Model):
    ismi = models.CharField(max_length=200)
    sharifi = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telefon = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Yo'lovchilar"

    def __str__(self) -> str:
        return self.ismi


class Band_qilish(models.Model):
    yolovchi = models.OneToOneField(Yolovchi, on_delete=models.CASCADE)
    chipta = models.ForeignKey(Chipta, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Band_qilishlar"


@receiver(post_save, sender=User)
def create_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
