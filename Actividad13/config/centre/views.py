from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'head/index.html')

def professors(request):
    professors = [
        {"name": "Davids", "surname": "Ismael", "email": "davids@gmail.com", "age": "20", "genero": "Masculino"},
        {"name": "Daniel", "surname": "Cubias", "email": "daniel@gmail.com", "age": "25", "genero": "No especificado"},
        {"name": "Ahmed", "surname": "Aziz", "email": "Ah39aziz@gmail.com", "age": "20", "genero": "Masculino"}
    ]
    return render(request, 'professors.html', {'professors': professors})

def alumnos(request):
    usrs = [
        {"name": "Ana", "surname": "Perez", "email": "correoAna@gmail.com" ,"Curs": "DAW2B" ,"age": 22},
        {"name": "Carlos", "surname": "Gomez", "email": "correoCarlos@gmail.com" ,"Curs": "DAW2B", "age": 19},
        {"name": "Maria", "surname": "Lopez", "email": "correoMaria@gmail.com" ,"Curs": "DAW2B", "age": 23}
    ]
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
