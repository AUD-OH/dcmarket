from django.urls import path
from accounts import views

from accounts import views as accounts_views  # Importing views from accounts app

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('follow/<int:user_id>/', views.follow_view, name='follow'),
]

