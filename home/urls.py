from django.conf.urls import url
from django.urls import path
from .views import *



urlpatterns = [
        path('', homeView, name= 'home'),
        path('getsession/', getsession, name= 'getsession'),
        path('setsession/', setsession, name= 'setsession'),
        path('delsession/', delsession, name= 'delsession'),
        path('clearcart/', clearCart, name= 'clearcart'),
        path('addtocart/', addtoCart, name= 'addtocart'),
        path('addtocartfromdet/', addtoCartFromDet, name= 'addtocartfromdet'),
        path('cartview/', cartView, name= 'cartview'),
        path('shopview/', shopView, name= 'shopview'),
        path('productdetail/<int:id>', productDetail, name= 'productdetail'),
        path('delitem/', delItem, name= 'delitem'),
]