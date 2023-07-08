from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Product, Category


# Create your views here.
def shop_index(request: HttpRequest) -> HttpResponse:
    # select_related - загружать при связи К ОДНОМУ, как joinedload (INNER JOIN)
    products = (Product
                .objects
                .filter(~Q(status=Product.Status.ARCHIVED))
                .order_by("id")
                .select_related("category")
                .defer("description",
                       "created_at",
                       "updated_at",
                       "category__description")  # Не загружать поле description у таблицы category
                .all())
    return render(
        request,
        template_name="shop/index.html",
        context={"products": products},
    )


def categories_with_products_tree(request: HttpRequest) -> HttpResponse:
    # prefetch_related - Запрос ко многим
    categories = (
        Category.objects.order_by("id").prefetch_related("products").all()
    )
    return render(
        request,
        template_name="shop/categories-with-products-tree.html",
        context={"categories": categories},
    )
