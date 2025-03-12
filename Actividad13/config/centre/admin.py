
from .models import Alumne,Professors
from django.contrib import admin

## el name, surname ,email, tienen que ser los mismos que en el models

@admin.register(Alumne)
class alumnes(admin.ModelAdmin):
    list_display = ('name', 'surname', 'surname2', 'email', 'curs', 'modulsMatriculats'  )


@admin.register(Professors)
class professor(admin.ModelAdmin):
    list_display = ('name', 'surname', 'surname2', 'email', 'curs' , 'tutor', 'moduls_repartits')

