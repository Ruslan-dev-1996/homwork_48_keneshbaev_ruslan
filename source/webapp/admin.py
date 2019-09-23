from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk',  'description', 'category', 'amount']
    list_filter = [ 'category']
    fields = [ 'name',  'description',  'category', 'amount', 'price']




admin.site.register(Product, ProductAdmin)
