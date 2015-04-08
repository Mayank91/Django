from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from models import Expence
import json
import datetime

def index(request):
    expense_objs = Expence.objects.all()
    expenses = {}
    for expenses_obj in expense_objs:
        m = expenses_obj.date.strftime('%B')
        if expenses.has_key(m):
            expenses[m]['expenses'].append(expenses_obj)
            expenses[m]['total'] += expenses_obj.money
        else:
            expenses[m] = {'expenses': [expenses_obj]}
            expenses[m]['total'] = expenses_obj.money

    for month in expenses:
        print month ,"=",  expenses[month]
    expenses={"expenses":expenses}
    return render(request,'index.html',expenses)

#def month(request,pk):
    #mon = get_object_or_404(Expence,pk = pk)

 #   return HttpResponse("monthfelk")
