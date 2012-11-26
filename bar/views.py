from django.template import Context, loader
from bar.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
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
    
def orderdetail(request, order_id):
    orderdetail_list = OrderItem.objects.filter(order=order_id)
    return render_to_response('bar/orderdetail.html', {'orderdetail_list': orderdetail_list})
    
def drink(request, bar_id, drink_id):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = Order(bar = Bar.objects.get(pk=request.POST['bar']))
            order.save()
            #if request.POST['new'] == 'new':
            #order = Order.objects.get(pk=request.POST['order'])
            drink = Drink.objects.get(pk=request.POST['drink'])
            quantity = request.POST['quantity']
            orderitem = OrderItem(order=order, drink=drink, quantity=quantity)
            orderitem.save()
            orderid = orderitem.order
            return render(request, '/bar/bar' bar_id)
    else:
        form = OrderForm(initial={'drink': drink_id, 'bar': bar_id }) # An unbound form
    return render(request, 'bar/drink.html', { 'form': form })
    
    
    