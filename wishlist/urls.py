from django.urls import path, include
from . import views

urlpatterns = [
    path('move_to_bag/<int:item_id>/', views.move_to_bag, name='move_to_bag'),
    path('', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_from_wishlist/<int:wishlist_id>/', views.delete_from_wishlist, name='delete_from_wishlist'), 
]
