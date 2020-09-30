from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main"),
    path('about/', views.about_page, name="about"),
    path('price/', views.price_page, name="price"),
    path('contacts/', views.contacts_page, name="contacts"),
    path('partners/', views.partners_page, name="partners"),
]