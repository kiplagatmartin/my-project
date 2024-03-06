from django.contrib import messages
from django.shortcuts import render, redirect
from shamba.models import Product, Item
from .forms import customerform


# Create your views here.


def signup(request):
    form = customerform()
    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    context = {'form': form}
    return render(request, 'signup.html', context)


def items(request):
    context = {'product': Product.objects.all()}
    return render(request, 'items.html', context)


def cart(request):
    cart_item = Item.objects.filter(user=request.user)
    total_price = sum(item.price * item.quantity for item in cart_item)
    return render(request, 'cart.html', {'cart_item': cart_item, 'total_price': total_price})


def add_to_cart(request, product_id):
    item = Product.objects.get(id=product_id)
    cart_item = Item.objects
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_items', {'item': item})


def remove_from_cart(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.quantity -= 1
        item.delete()
        return redirect('cart:view_items', {'item': item})
    return redirect('cart:view_items', {'item': item})


def payment(request):
    item = Item.objects.get()
    # i = item.objects.all()
    if request.method == 'POST':
        # mc = MpesaClient()
        # number = request.POST.get('number')
        # amount = Product.price
        # transaction_description = 'purchase'
        #  callback_URL = request.POST.get()
        messages.success(request, f'you have successfully purchased your items')
        return redirect('items:view_items', {'item': item})

    else:
        payform = cart(request)
        return render(request, 'payment.html', {'payform': payform})
