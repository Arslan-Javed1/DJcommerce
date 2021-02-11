from django import template
from django.shortcuts import get_object_or_404
from ..models import Product 

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False
    

@register.filter(name='how_many_in_cart')
def how_many_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            cartGet = cart.get(id)
            return cartGet
    return 0

@register.filter(name='cal_total')
def cal_total(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            cartGet = cart.get(id)
            total = product.price*cartGet
            return float(total)
    return 0

    