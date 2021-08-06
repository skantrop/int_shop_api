from django.contrib import admin
from .models import *


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class AdminProductDisplay(admin.ModelAdmin):
    readonly_fields = ('slug', )
    fields = ('slug', 'title', 'description', 'price', 'category', 'author')
    search_fields = ('title', )
    inlines = (ProductImageInLine, )


@admin.register(Category)
class AdminCategoryDisplay(admin.ModelAdmin):
    readonly_fields = ('slug', )
    fields = ('slug', 'title')
    search_fields = ('title', )


admin.site.register(Review)
admin.site.register(Favorite)
