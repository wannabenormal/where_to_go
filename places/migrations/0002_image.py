# Generated by Django 3.0 on 2022-05-11 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1, verbose_name='Порядок')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place', verbose_name='Место')),
            ],
        ),
    ]