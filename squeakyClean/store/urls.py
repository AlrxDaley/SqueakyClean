from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import about, contact, index, shop


urlpatterns = [
    path('', index, name='index'),
    path('index/', index , name='index'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
]
