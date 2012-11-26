from django.template import Context, loader
from bar.models import Bar, Drink, Order, OrderItem
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext

def home(request):
    bars_list = Bar.objects.all().order_by('id')
    return render_to_response('bar/barlist.html', {'bars_list': bars_list})
    
def menu(request, bar_id):
    menu_list = Drink.objects.filter(bar=bar_id)
    return render_to_response('bar/menu.html', {'menu_list': menu_list})
    
def orders(request, bar_id):
    orders_list = Order.objects.filter(bar=bar_id)
    return render_to_response('bar/orders.html', {'orders_list': orders_list})
    
#def orderdetail(request, order_id):
#    orderdetail_list = OrderItem.objects.filter(order=order_id)
#    return render_to_response('bar/drink.html', {'drink': drink})
    
def drink(request, drink_id):
    drink = Drink.objects.filter(id=drink_id)
    return render_to_response('bar/drink.html', {'drink': drink})