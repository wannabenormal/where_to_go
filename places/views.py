from django.shortcuts import render
from .models import Place


def render_home_page(request):
    context = {
        "places_geodata": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.longitude, place.latitude]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": ''
                    }
                }
                for place in Place.objects.all()
            ],
        }
    }
    return render(request, 'places/home.html', context)
