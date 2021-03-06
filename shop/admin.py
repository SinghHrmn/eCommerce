from django.contrib import admin
from .models import Product,Category,CartTable

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','mrp','is_featured','is_on_sale')
    list_editable = ('is_on_sale','is_featured', 'mrp','price')
    list_display_links = ('id','product_name')
    list_filter = ('category_name',)

# Register your models here.
admin.site.register(Product, ProductsAdmin)
admin.site.register(Category)
admin.site.register(CartTable)