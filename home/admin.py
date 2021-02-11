from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug': ('name','category')}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'subcategory', 'price', 'quantity', 'available', 'timeStamp', 'slug']
    list_filter = ['available', 'timeStamp']
    list_editable = ['price', 'quantity', 'available']
    prepopulated_fields = {'slug': ('name','category','subcategory')}

    


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)