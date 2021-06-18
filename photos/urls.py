from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about',),
    path('photo/<int:photo_id>/', show_photo, name='photo'),
    path('category/<int:category_id>/', show_category, name='category'),
    path('search_title', search_title, name='search-title'),
]