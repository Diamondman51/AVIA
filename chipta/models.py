from random import randint
from django.db import models

# Create your models here.


class Chipta(models.Model):
    raqam = models.PositiveBigIntegerField(unique=True, null=False)
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
