from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-list-view'),
    path('search/', views.search_post, name='blog-search-post'),
]