from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Order, Restaurant
from django.utils import timezone
from .forms import OrderForm
from django.shortcuts import redirect


def order_list(request):
    orders = Order.objects.filter(made_on__lte=timezone.now()).order_by('made_on')
    return render(request, 'zakaz/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'zakaz/order_detail.html', {'order': order})

def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.made_on = timezone.now()
            order.status = 'A'
            order.save()
        return redirect('order_detail', pk=order.id)
    else:
        form = OrderForm()
    return render(request, 'zakaz/order_new.html', {'form': form})
