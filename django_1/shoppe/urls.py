from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='Shoppe-Home'),
    path('about/',views.about,name='Shoppe-About'),
]
