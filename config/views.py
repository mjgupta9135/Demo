from django.http import HttpResponse
from django.shortcuts import render

from emp.models import Employee


def home(request):
    emp=Employee.objects.all()
    context={
        'employees':emp
    }
    return render(request,'home.html',context)
