from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from models import Expence
import datetime
def index(request):
    obj = Expence.objects.all()
    j = 0
    k = 0
    for i in obj:
        m = i.date.strftime('%B')
        if m == "March":
            j = j + i.money
        elif m == "April":
            k = k + i.money

    context = {'obje' : obj,'j':j,'m' : m,'k':k}
    return render(request,'index.html',context)

#def month(request,pk):
    mon = get_object_or_404(Expence,pk = pk)

 #   return HttpResponse("monthfelk")
