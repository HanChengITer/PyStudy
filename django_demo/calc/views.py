from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def example(request):
    #return HttpResponseRedirect(reverse('calc_index'))
    return HttpResponseRedirect(reverse('calc_add',args=(3,4)))

def cal_index(request):
#    return HttpResponse('可以使用/calc/add/3/4<br>也可以使用/calc/add?x=3&y=4')
    return render(request,'calc_index.html')

def add_with_params(request):
    x=request.GET['x']
    y=request.GET['y']
    return HttpResponse("{} + {} = {}".format(x,y,int(x)+int(y)))

def add(request,x,y):
    #return HttpResponse(x,'+',y,'=',int(x)+int(y))
    return HttpResponse("{} + {} = {}".format(x,y,int(x)+int(y)))
