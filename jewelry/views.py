from django.template import Context, loader
from jewelry.models import Jewelry
from django.http import HttpResponse

def index(request):
    jewelry_list = Jewelry.objects.all().order_by('id')[:5]
    t = loader.get_template('jewelry/index.html')
    c = Context({
        'jewelry_list': jewelry_list,
    })
    return HttpResponse(t.render(c))
    
def detail(request, item_id):
    try:
        p = Jewelry.objects.get(pk=item_id)
    except Jewelry.DoesNotExist:
        raise Http404
    return render_to_response('jewelry/detail.html', {'item': p})
