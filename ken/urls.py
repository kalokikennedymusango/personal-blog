from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('services/', views.services, name = 'services'),
    path('joinus/', views.joinus, name = 'joinus'),
    path('footer/', views.footer, name = 'footer'),
    path('review/', views.review, name = 'review'),
    path('contacts/', views.contacts, name = 'contacts'),
]