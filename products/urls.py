from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # path('<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
