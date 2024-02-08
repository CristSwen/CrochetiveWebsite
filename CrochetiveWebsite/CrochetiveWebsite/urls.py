"""
Definition of urls for CrochetiveWebsite.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import (home, contact, about, shop, create_product_apparel, create_product_toys, create_product_pets, edit_product, delete_product)



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('create_apparel/', views.create_product_apparel, name='create_apparel'),
    path('create_pets/', views.create_product_pets, name='create_pets'),
    path('create_toys/', views.create_product_toys, name='create_toys'),
    path('edit_product/', views.edit_product, name='edit_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('apparel_shop/', views.shop_apparel, name='shop_apparel'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
