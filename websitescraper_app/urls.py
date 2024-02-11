from django.urls import path

from websitescraper_app import views


urlpatterns = [
    path('',views.home,name='home'),
]