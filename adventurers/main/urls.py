
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-as', views.about, name='about'),
    path('create', views.create, name='create'),
    path('book_Of_The_Dead', views.book_Of_The_Dead, name='book'),
    path('saga_story', views.saga_story, name='story'),
    path('tvorchestvo', views.tvorchestvo, name='tvorchestvo'),
]
