from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Fling, Sender, Media
from controller import Api

# Create your views here.
def index(request):
   # return HttpResponse("hello this is the index")

    flings = Fling.objects.order_by('-created_at')
    template = loader.get_template('home/index.html')
    context = RequestContext(request, {
        'flings': flings,
    })
    return HttpResponse(template.render(context))

def update(request):
    a = Api()
    flings = a.getNewItems()
    return HttpResponse(flings)

def detail(request):
    f_id= request.GET.get('id','')
    fling = Fling.objects.get(id=f_id)
    template = loader.get_template('home/details.html')
    context = RequestContext(request, {
        'fling': fling,
    })

    return HttpResponse(template.render(context))



