from django.urls import path, include
from . import views

# 원래는 path('users/', views.users) 필요한데 이미 users 안이니까 지워도됌
urlpatterns = [
    path('', views.users, name='users'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
