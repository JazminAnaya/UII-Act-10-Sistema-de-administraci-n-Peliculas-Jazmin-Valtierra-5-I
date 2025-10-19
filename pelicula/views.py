from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pelicula
from .forms import PeliculaForm

# Vista principal: muestra todas las películas
def index(request):
    return render(request, 'pelicula/index.html', {
        'peliculas': Pelicula.objects.all()
    })

# Vista para ver una película
def view_pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id_pelicula=id_pelicula)
    return HttpResponseRedirect(reverse('index'))

# Vista para agregar una nueva película
def add(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pelicula/add.html', {
                'form': PeliculaForm(),
                'success': True
            })
    else:
        form = PeliculaForm()
    return render(request, 'pelicula/add.html', {'form': form})

# Vista para editar una película
def edit(request, id_pelicula):
    pelicula = Pelicula.objects.get(id_pelicula=id_pelicula)

    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return render(request, 'pelicula/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = PeliculaForm(instance=pelicula)

    return render(request, 'pelicula/edit.html', {'form': form})

def delete(request, id_pelicula):
    if request.method == 'POST':
        pelicula = Pelicula.objects.get(id_pelicula=id_pelicula)
        pelicula.delete()
    return HttpResponseRedirect(reverse('index'))
