from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('category/<slug>', views.category, name='category'),
    path('blog', views.blog, name='blog'),
]
