from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog')
]
