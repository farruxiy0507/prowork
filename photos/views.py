from django.shortcuts import render, get_object_or_404
from .models import Photos, Category


def homepage(request):
    photos = Photos.objects.all()
    cats = Category.objects.all()
    context = {
        'photos': photos,
        'cats': cats,
        'title': 'Homepage',

    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': 'About page',
    }
    return render(request, 'about.html', context)


def show_photo(request, photo_id):

    ph = get_object_or_404(Photos, pk=photo_id)
    context = {
        'photos': ph,
        'title': ph.title,
        'cat_selected': ph.category_id
    }
    return render(request, 'photo.html', context)


def show_category(request, category_id):
    photos = Photos.objects.filter(category_id=category_id)
    cats = Category.objects.all()

    context = {
        'photos': photos,
        'cats': cats,
        'title': 'Category',
        'cat_selected': category_id,

    }
    return render(request, 'home.html', context)


def search_title(request):
    cats = Category.objects.all()
    if request.method == "POST":
        searched_photo = request.POST['searched']
        titlesOfSearchedPhoto = Photos.objects.filter(title__contains=searched_photo)
        context = {
            'cats': cats,
            'searched': searched_photo,
            'photos': titlesOfSearchedPhoto
        }
        return render(request, 'search_title.html', context)
    else:
        return render(request, 'search_title.html', {})






