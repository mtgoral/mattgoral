from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request) :
    return render_to_response("index.html")
    
def work(request) :
    return render_to_response("work.html")
    
def resume(request) :
    return render_to_response("resume.html")
    
def about(request) :
    return render_to_response("about.html")
    
def contact(request) :
    return render_to_response("contact.html")
    
def blinq(request) :
    return render_to_response("blinq.html")
    
def fivelines(request) :
    return render_to_response("5lines.html")
    
def wcc(request) :
    return render_to_response("wcc.html")