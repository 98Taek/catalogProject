def cart(request):
    cart = request.session.get('cart', {})

    return {
        'cart': list(cart.values()),
    }