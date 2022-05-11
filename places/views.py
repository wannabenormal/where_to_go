from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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


def get_detail_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    return JsonResponse(
        {
            "title": place.title,
            "imgs": [
                image.image.url
                for image in place.images.all().order_by('order')
            ],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude,
            }
        },
        json_dumps_params={'ensure_ascii': False}
    )
