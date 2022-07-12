from django.urls import path, include
from . import views
from bag.views import add_to_bag

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
     path('add/<item_id>/', add_to_bag, name='add_to_bag'),
]