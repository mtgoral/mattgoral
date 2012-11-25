from django.template import Context, loader
from bar.models import Bar, Drink
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404

def home(request):
    bars_list = Bar.objects.all().order_by('id')
    return render_to_response('bar/barlist.html', {'bars_list': bars_list})
    
def menu(request, bar_id):
    return HttpResponse("You're looking at %s." % bar_id)