from django.shortcuts import render, get_object_or_404

from shop.models import Product


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
