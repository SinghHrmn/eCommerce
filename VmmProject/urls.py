"""VmmProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .mycontrollers import *

urlpatterns = [
    path('', include('shop.urls')),
    path('shop/', include('shop.urls')),
    path('cgxuvimr/admin/ajay/', admin.site.urls),
    path('add-admin', addAdmin),
    path('add-admin-action', addAdminAction),
    path('view-admin', viewAdmin),
    path('view-admin-action', viewAdminAction),
    path('edit-admin', editAdmin),
    path('edit-admin-action', editAdminAction),
    path('save-admin', saveAdmin),
    path('delete-admin-action', deleteAdminAction),
    path('add-category', addCategory),
    path('add-category-action', addCategoryAction),
    path('view-category', viewCategory),
    path('view-category-action', viewCategoryAction),
    path('edit-category', editCategory),
    path('edit-category-action', editCategoryAction),
    path('save-category', saveCategory),
    path('delete-category-action', deleteCategoryAction),
    path('user-signup', userSignup),
    path('user-signup-action', userSignupAction),
    path('add-product', addProduct),
    path('add-product-action', addProductAction),
    path('view-product', viewProduct),
    path('view-product-action',viewProductAction),
    path('delete-product-action', deleteProductAction),
    path('view-allproducts', viewAllProducts),
    path('view-allproduct-action', viewAllProductsAction),
    path('add-to-cart-action', addtoCartAction),
    path('my-cart', myCart),
    path('my-cart-action', myCartAction),
    path('login', userLogin),
    path('login-action', userLoginAction),
    path('proceedtopay', proceedtoPay),
    path('user-homepage', userHomePage),
    path('billinfo', billinfo),
    path('logout', logout),
    path('checkoutaction', checkoutaction),
    path('thankspage', thankspage),
    path('pending-orders', pendingorders),
    path('pending-order-action', pendingordersaction),
    path('thankspage', thankspage),
    path('my-orders', myorder),
    path('myordersaction', myordersaction),
    path('approve_reject_action', approve_reject_action),
    path('account/',include('accounts.urls')),
    path('about/',include('about.urls')),
    path('update/', updatedata),
    path('updated/', updated),
]
