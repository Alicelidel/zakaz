from django.contrib import admin
from .models import Order, Dish, Restaurant

admin.site.register(Order)
admin.site.register(Dish)
admin.site.register(Restaurant)
# Register your models here.
