from django.shortcuts import render
from .models import Category, Photo


def home(request):
    photos = Photo.objects.all().order_by('-id')[:6]
    return render(request, 'gallery/home.html', {'photos': photos})


def portfolio(request, category_slug=None):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    if category_slug:
        photos = photos.filter(category__slug=category_slug)

    context = {
        'categories': categories,
        'photos': photos,
        'current_category': category_slug,
    }

    if request.headers.get('HX-Request'):
        return render(request, 'gallery/partials/photo_list.html', context)

    return render(request, 'gallery/portfolio.html', context)
