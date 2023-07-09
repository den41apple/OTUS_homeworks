from django.db.models import Q
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Category
from .models import Product


class CategoriesListView(ListView):
    model = Category
    queryset = Category.objects.filter(~Q(archived=True)).all()


class CategoryDetailView(DetailView):
    model = Category


class ShopIndexView(TemplateView):
    template_name = "shop/index.html"


class ProductsView(ListView):
    template_name = "shop/products.html"
    queryset = (
        Product.objects.filter(~Q(status=Product.Status.ARCHIVED))
        .order_by("id")
        .select_related("category")
        .defer(
            "description",
            "created_at",
            "updated_at",
            "category__description",
        )
        .all()
    )
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
