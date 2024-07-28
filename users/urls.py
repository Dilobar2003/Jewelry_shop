from django.urls import path
from .views import  registration_view, login_view, logout_view, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),


    path('register/', registration_view, name='register'),

]