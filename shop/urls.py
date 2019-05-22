from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.all_products, name='products'),
    path('product/<int:product_id>', views.product,  name='product'),
    path('viewcart', views.view_cart, name='cart'),
    path('addtocartaction', views.addtocartaction),
    path('addtocartaction2', views.demo),
]
