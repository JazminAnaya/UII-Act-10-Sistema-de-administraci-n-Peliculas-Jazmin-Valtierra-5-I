from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo_pelicula', 'genero', 'duracion', 'clasificacion', 'sinopsis']
        labels = {
            'titulo_pelicula': 'Título de la Película',
            'genero': 'Género',
            'duracion': 'Duración (minutos)',
            'clasificacion': 'Clasificación',
            'sinopsis': 'Sinopsis'
        }
        widgets = {
            'titulo_pelicula': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
