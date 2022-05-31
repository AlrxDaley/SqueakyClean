from django.urls import path
from .views import about, index


urlpatterns = [
    path('', index, name='index'),
    path('', about, name='about'),
    
]
