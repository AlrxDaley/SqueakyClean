"""squeakyClean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
import profile.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('index/', include('store.urls')),
    path('contact/', include('contactEmail.urls')),
    path('about/', include('store.urls')),
    path('shop/', include('store.urls')),
    path('contact/', include('store.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')), 
    path('register-success/', profile.views.register_success, name='register-success'), 
    path("register/", profile.views.register_request, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
