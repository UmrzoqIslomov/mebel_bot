from django.contrib import admin
from .models import Category, Product, Savat, SubCategory, Made_in

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Made_in)
admin.site.register(Product)
admin.site.register(Savat)