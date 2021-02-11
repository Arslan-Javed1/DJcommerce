#from home.templatetags.cart import grand_total
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.http import JsonResponse





def homeView(request):

    cat_id = request.GET.get('cat')
    if cat_id:
        products = Product.get_products_by_cat(cat_id)
    else:
        products = Product.get_all_products()
    
    categories = Category.get_all_categories()
    cart = request.session.get('cart')
    if cart:
        keys = cart.keys()
        cart_items = []
        grand_total = 0
        for id in keys:
            cart_item = get_object_or_404(Product, id = id)
            cart_items.append(cart_item)
            how_many_in_cart = cart.get(id)
            total = cart_item.price*how_many_in_cart
            grand_total += total
        return render(request, 'home.html', {'products':products, 'categories': categories, 'cart_items': cart_items, 'grand_total': grand_total})
    else:
        return render(request, 'home.html', {'products':products, 'categories': categories})

def addtoCart(request):
    print('I am innnnnnnnnnnnnnnn')
    if (request.method == 'POST'):
        remove = request.POST.get('remove')
        product = request.POST.get('prod_id')
        cart = request.session.get('cart')
        if cart:
            quant = cart.get(product)
            if quant:
                if remove:
                    if quant <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quant - 1
                else:
                    cart[product] = quant + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])

        data = {
        'cart': cart,
        }

        return JsonResponse(data)

def addtoCartFromDet(request):
    print('I am innnnnnnnnnnnnnnn')
    if (request.method == 'POST'):
        product = request.POST.get('prod_id')
        cart = request.session.get('cart')
        if cart:
            quant = cart.get(product)
            if quant:
                cart[product] = quant + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])

        data = {
        'cart': cart,
        }

        return redirect('cartview')


def delItem(request):
    if (request.method == 'POST'):
        product = request.POST.get('prod_id')
        cart = request.session.get('cart')
        if cart:
            cart.pop(product)
        request.session['cart'] = cart
        print(request.session['cart'])
        data = {
        'cart': cart,
        }

        return redirect('cartview')





def cartView(request):
    cart = request.session.get('cart')
    if cart:
        keys = cart.keys()
        products = []
        grand_total = 0.0
        for id in keys:
            product = get_object_or_404(Product, id = id)
            print(product)
            products.append(product)
            how_many_in_cart = cart.get(id)
            total = product.price*how_many_in_cart
            grand_total += total
        
        return render(request, 'cart.html', {'products':products, 'grand_total': grand_total})
    else:
        return render(request, 'cart.html')
    





def productDetail(request, id):
    product = get_object_or_404(Product, id = id)
    print('kkkkkkkkkkkkkk: ', product.name)
    cart = request.session.get('cart')
    if cart:
        keys = cart.keys()
        cart_items = []
        for id in keys:
            cart_item = get_object_or_404(Product, id = id)
            cart_items.append(cart_item)
        return render(request, 'product_detail.html', {'product':product, 'cart_items':cart_items})
    else:
        return render(request, 'product_detail.html', {'product':product})

def shopView(request):
    cat_id = request.GET.get('cat')
    if cat_id:
        products = Product.get_products_by_cat(cat_id)
    else:
        products = Product.get_all_products()
    
    categories = Category.get_all_categories()
    cart = request.session.get('cart')
    if cart:
        keys = cart.keys()
        cart_items = []
        for id in keys:
            cart_item = get_object_or_404(Product, id = id)
            cart_items.append(cart_item)
        return render(request, 'shop.html', {'products':products, 'cart_items':cart_items})
    else:
        return render(request, 'shop.html', {'products':products,'categories': categories})



def clearCart(request):
    request.session.clear()
    return redirect('/')


def setsession(request):
    request.session['name'] = 'King'
    return render(request, 'set_session.html')

def setsession(request):
    request.session['name'] = 'King'
    return render(request, 'set_session.html')


def getsession(request):
    name = request.session.get('name', default= 'Guest')
    return render(request, 'get_session.html', {'name': name})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'del_session.html')
