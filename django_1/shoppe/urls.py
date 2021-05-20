from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='Shoppe-Home'),
    path('about/',views.about,name='Shoppe-About'),
    path('electronics/',views.electronics,name='electronics'),
    path('fashion/',views.fashion,name='fashion'),
    path('grocery/',views.grocery,name='grocery'),
    path('sucessful_buy/',views.successful_buy,name='success'),
]
