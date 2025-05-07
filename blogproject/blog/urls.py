from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='postList'),
    path('post/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/create/', views.postCreate, name='postCreate'),
    path('post/edit/<int:pk>/', views.postEdit, name='postEdit'),
    path('post/delete/<int:pk>/', views.postDelete, name='postDelete'),
]
