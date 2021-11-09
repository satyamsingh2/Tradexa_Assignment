from django.urls import path
from .views import ProductListView, PostDetailView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/<int:product_id>/', PostDetailView.as_view(), name='product-detail'),
]