# Generated by Django 3.0 on 2022-05-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220513_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Название'),
        ),
    ]