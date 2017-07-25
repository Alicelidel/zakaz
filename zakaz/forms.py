from django import forms
from .models import Order, Dish, Restaurant

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('rest_name', 'consists_of', 'num_of_dishes',)
