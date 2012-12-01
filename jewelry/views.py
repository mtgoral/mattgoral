from django.template import Context, loader
from jewelry.models import Jewelry
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
    
def all(request):
    jewelry_list = Jewelry.objects.all().order_by('id')
    return render_to_response('jewelry/gallery.html', {'jewelry_list': jewelry_list})
    
def earrings(request):
    jewelry_list = Jewelry.objects.filter(category="E")
    return render_to_response('jewelry/gallery.html', {'jewelry_list': jewelry_list})
    
def bracelets(request):
    jewelry_list = Jewelry.objects.filter(category="B")
    return render_to_response('jewelry/gallery.html', {'jewelry_list': jewelry_list})
    
def rings(request):
    jewelry_list = Jewelry.objects.filter(category="R")
    return render_to_response('jewelry/gallery.html', {'jewelry_list': jewelry_list})
    
def necklaces(request):
    jewelry_list = Jewelry.objects.filter(category="N")
    return render_to_response('jewelry/gallery.html', {'jewelry_list': jewelry_list})
    
def about(request):
    return render_to_response('jewelry/about.html')
    
def detail(request, item_id):
    try:
        p = Jewelry.objects.get(pk=item_id)
    except Jewelry.DoesNotExist:
        raise Http404
    return render_to_response('jewelry/detail.html', {'item': p})
    
def all(request):
    jewelry_list = Jewelry.objects.all().order_by('id')
    return render_to_response('jewelry/gallery.html', {'jewelry_list': jewelry_list})
    
def all(request) :
    return render_to_response("fuckyou.html")
