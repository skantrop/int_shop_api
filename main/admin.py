from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Cart)