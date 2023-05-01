from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-list-view'),
    path('add_post/', views.add_post, name='blog-add-post'),
    path('read/<int:pk>/', views.read_post, name='blog-read-post'),
    path('search/', views.search_post, name='blog-search-post'),
]