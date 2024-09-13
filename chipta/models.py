from django.db import models

# Create your models here.


class Chipta(models.Model):
    raqam = models.BigIntegerField(unique=True)
    kompaniya = models.CharField(null=False, max_length=200)
    ketish_vaqti = models.DateTimeField()
    kelish_vaqti = models.DateTimeField()
    qaysi_shaharga = models.CharField(max_length=150)
    qaysi_shahardan = models.CharField(max_length=150)
    is_reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Chiptalar'

    def __str__(self):
        return f'{self.raqam}'


class Yolovchi(models.Model):
    ismi = models.CharField(max_length=100)
    sharifi = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefon = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Yo\'lovchilar'

    def __str__(self):
        return f'{self.ismi}'


class Band_qilish(models.Model):
    yolovchi = models.ForeignKey(Yolovchi, on_delete=models.CASCADE)
    chipta = models.OneToOneField(Chipta, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Band_qilishlar'
