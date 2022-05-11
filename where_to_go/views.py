from django.shortcuts import render


def render_home_page(request):
    return render(request, 'home.html')
