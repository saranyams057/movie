
from django.http import HttpResponse
from django.shortcuts import render
from . models import places
from . models import team
def demo(request):
    obj=places.objects.all()
    obj1=team.objects.all()
    dic={'result':obj,'res':obj1}
    return render(request,"index.html",dic)
