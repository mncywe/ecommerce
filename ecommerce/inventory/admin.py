from django.contrib import admin
from ecommerce.inventory.models import (
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductInventory,
    Stock,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Media)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductInventory)
admin.site.register(Stock)
