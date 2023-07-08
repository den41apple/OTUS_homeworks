from datetime import datetime

from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    # id primary key django ставит автоматически
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Status(models.IntegerChoices):
        ARCHIVED = 0
        AVAILIBLE = 1

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)
    expiration_date = models.DateField(default=datetime.fromtimestamp(0))
    description = models.TextField()
    category = models.ForeignKey(  # related_name это имя у другой модели
        Category, on_delete=models.PROTECT, related_name="products"
    )
    status = models.IntegerField(choices=Status.choices)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Product <{self.id}, {self.name!r}>"
