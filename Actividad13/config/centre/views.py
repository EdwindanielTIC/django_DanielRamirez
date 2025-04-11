from lib2to3.fixes.fix_input import context

from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AlumneForm, ProfessorsForm
from .models import Alumne, Professors

def index(request):
    usrs = Alumne.objects.all()  # Obtiene todos los alumnos
    return render(request, 'index.html', {'alumnes': usrs})

def professors(request):
        prof = Professors.objects.all()
        return render(request, 'professors.html', {'professors': prof})

def alumnos(request):
    usrs = Alumne.objects.all()
    return render(request, 'alumnos.html', {'usrs': usrs})


    # esto hace que me cree los datos directamente, y luego me los devuelva a la pagina web
def user_form(request):
    form = AlumneForm()

    if request.method == 'POST':
        form = AlumneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    context = {'form': form}
    return render(request, 'forms.html', context)


def professor_form(request):
        form = ProfessorsForm()

        if request.method == 'POST':
            form = ProfessorsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        context = {'form': form}
        return render(request, 'forms.html', context)


def details(request, pk):
    alumne_obj = None
    try:
        alumne_obj = Alumne.objects.get(pk=pk)  # Busca el alumno por ID
    except Alumne.DoesNotExist:
        alumne_obj = None
    return render(request, 'details.html', {'alumne': alumne_obj})

#
# Professors

def detailsProfesors(request, pk):
    profesors_obj = None
    try:
        profesors_obj = Professors.objects.get(pk=pk)
    except Professors.DoesNotExist:
        profesors_obj = None
    return render(request, 'detailsProfesors.html', {'professors': profesors_obj})