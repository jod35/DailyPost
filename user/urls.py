from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='user_home'),
    path('profile/',views.profile,name='user_profile'),
    path('signup/',views.signup,name='user_signup'),
    path('about/',views.about,name='user_about'),
]