from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='user_home'),
    path('about/',views.about,name='user_about'),
]