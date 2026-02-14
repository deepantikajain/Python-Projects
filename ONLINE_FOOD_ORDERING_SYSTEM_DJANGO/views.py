from django.shortcuts import render, redirect
from .models import Restaurant, FoodItem, Cart, Order

from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    
    if query:
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=query) |
            Q(fooditem__name__icontains=query)
        ).distinct()
    else:
        restaurants = Restaurant.objects.all()

    return render(request, 'home.html', {'restaurants': restaurants})



def menu(request, restaurant_id):
    items = FoodItem.objects.filter(restaurant_id=restaurant_id)
    return render(request, 'menu.html', {'items': items})


def add_to_cart(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')



def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.item.price * item.quantity for item in cart_items)

    Order.objects.create(
        user=request.user,
        total_price=total,
        payment_method="COD"
    )

    cart_items.delete()
    return render(request, 'success.html')


def increase_quantity(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def decrease_quantity(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('cart')

