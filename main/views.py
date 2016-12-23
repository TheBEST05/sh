from django.shortcuts import render
from main.models import Product


def home(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'home.html', context)


def product(request, p_id):
	product = Product.objects.get(id=p_id)
	context = {'product': product}
	return render(request, 'product.html', context)
