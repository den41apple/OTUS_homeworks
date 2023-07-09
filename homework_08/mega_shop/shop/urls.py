from django.urls import path
from .views import (
    ShopIndexView,
    ProductsView,
    ProductDetailView,
    CategoriesListView,
    CategoryDetailView,
)

app_name = "shop"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("categories/<int:pk>", CategoryDetailView.as_view(), name="category"),
]
