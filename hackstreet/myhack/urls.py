from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('chat/', views.chat, name='chat'),
    path('projects/', views.projects, name='projects'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('skills/', views.skills, name='skills'),
]
