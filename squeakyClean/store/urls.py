from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import about, contact, index, shop
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('index/', index , name='index'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
