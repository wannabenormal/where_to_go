import os

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place

import requests


class Command(BaseCommand):
    help = 'Parse places from json file'

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['json_path'])
        response.raise_for_status()
        place_response = response.json()

        place, created = Place.objects.update_or_create(
            title=place_response['title'],
            defaults={
                'description_short': place_response['description_short'],
                'description_long': place_response['description_long'],
                'longitude': place_response['coordinates']['lng'],
                'latitude': place_response['coordinates']['lat']
            }
        )

        if not created:
            place.images.all().delete()

        for img_url in place_response['imgs']:
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            place_image = place.images.create()
            place_image.image.save(
                os.path.basename(img_url),
                ContentFile(img_response.content),
                save=True
            )
