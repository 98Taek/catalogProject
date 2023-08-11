from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product


def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = {
        'quantity': 1,
        'price': str(product.price),
    }
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('shop:cart_detail')


def cart_detail(request):
    return render(request, 'cart/detail.html', {})
