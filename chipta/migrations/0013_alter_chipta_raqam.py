# Generated by Django 5.0.7 on 2024-09-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipta', '0012_delete_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chipta',
            name='raqam',
            field=models.PositiveBigIntegerField(),
        ),
    ]
