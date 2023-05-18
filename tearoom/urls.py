
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu_drinks/', views.menu_drinks, name='menu_drinks'),
    path('menu_snacks/', views.menu_snacks, name='menu_snacks'),
    path('cart/', views.cart, name='cart'),
    path('review/', views.ReviewList.as_view(), name='review'),
    path('review/create/', views.review, name='create'),

]