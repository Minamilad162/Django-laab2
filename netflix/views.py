from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movies
# Create your views here.

def index(request):
    movies = Movies.objects.all()
    return render(request, "netflix/index.html", {
        'movies' : movies
    })







def show(request, id):
    movie = Movies.objects.get(pk=id)
    return render(request, "netflix/show.html",{
        'movie' : movie  
})






def Create(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        return redirect("index")
    return render(request, "netflix/create.html",{
        'form' : form
    })


def delete(request, id):
    movie = Movies.objects.get(pk=id)
    movie.delete()
    return redirect("index")

def update(request, id):
    movie = Movies.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()

        return redirect("index")
    return render(request,"netflix/update.html", {
        'form': form,
        "movie": movie
    }) 

