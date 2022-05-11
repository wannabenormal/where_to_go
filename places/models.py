from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    order = models.IntegerField(default=1, verbose_name='Порядок')
    image = models.ImageField(verbose_name='Изображение')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )

    def __str__(self):
        return f'{self.order} {self.place.title}'
