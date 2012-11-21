from django.template import Context, loader
from jewelry.models import Jewelry
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
    
def index(request):
    jewelry_list = Jewelry.objects.all().order_by('id')
    return render_to_response('jewelry/index.html', {'jewelry_list': jewelry_list})
    
def detail(request, item_id):
    try:
        p = Jewelry.objects.get(pk=item_id)
    except Jewelry.DoesNotExist:
        raise Http404
    return render_to_response('jewelry/detail.html', {'item': p})
