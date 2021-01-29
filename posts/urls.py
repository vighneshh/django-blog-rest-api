# posts/urls.py
from django.urls import path
# from .views import PostList, PostDetail
from . import views

urlpatterns = [
# path('<int:pk>/', PostDetail.as_view()),
# path('', PostList.as_view()),
path('<int:pk>/', views.PostDetail, name='PostDetail'),
path('', views.PostList, name='PostList'),
]