# posts/urls.py
from django.urls import path
from .views import UserList, UserDetail
from . import views

urlpatterns = [

path('<int:pk>/', views.PostDetail, name='PostDetail'),
path('', views.PostList, name='PostList'),
path('users/', UserList.as_view()), # new
path('users/<int:pk>/', UserDetail.as_view()), # new
]