from django.shortcuts import render, redirect

from . form import MovieForm
from . models import Movies


# Create your views here.
def index(request):
    movie = Movies.objects.all()
    context = {'movie_list': movie}
    return render(request, "index.html", context)


def detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    context = {'object': movie}
    return render(request, "detail.html", context)


def add(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        decs = request.POST.get('decs', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie = Movies(name=name, decs=decs, year=year, img=img)
        movie.save()
    return render(request,"add.html")


def update(request,id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    #context = {'form': form, 'object': movie}
    return render(request, "edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method =="POST":
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")
