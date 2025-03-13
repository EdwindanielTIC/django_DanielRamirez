from lib2to3.fixes.fix_input import context

from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AlumneForm
from .models import Alumne, Professors


def index(request):
    return render(request, 'index.html')

def professors(request):
        prof = Professors.objects.all()
        return render(request, 'professors.html', {'professors': prof})



def alumnos(request):
    usrs = Alumne.objects.all()
    return render(request, 'alumnos.html', {'usrs': usrs})

bookstore = [
    {'id': 1, 'title': 'El Quijote', 'author': 'Cervantes'},
    {'id': 2, 'title': 'La llamada de lo salvaje', 'author': 'Gabriel Garcia Marquez'},
    {'id': 3, 'title': 'Viajo sin ver', 'author': 'John Z'}
]

def book(request, pk):
    book_Obj = None

    for i in bookstore:
        if i['id'] == pk:
            book_Obj = i
            break
    return render(request, 'book.html', {'book_Obj': book_Obj})

def books(request):
    return render(request, 'books.html', {'books': bookstore})


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