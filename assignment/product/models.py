from decimal import Decimal
from django.db.models import CharField, DecimalField, Model, DateTimeField
from django.core.validators import MinValueValidator


class Product(Model):
    name = CharField(max_length=150)
    weight = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    price = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    text = CharField(max_length=500, blank=True)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"