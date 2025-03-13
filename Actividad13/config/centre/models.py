from django.db import models
## esto es las tablas
## esto tiene que estar igual que en admin, el name, surname,email etc
# Create your models here.  UserName = admindaniel , PASSWORD=

class Alumne(models.Model):
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    surname2 = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    curs = models.DateField(max_length=500)
    modulsMatriculats = models.CharField(max_length=255, default='valor_por_defecto')



class Professors(models.Model):
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    surname2 = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    curs = models.CharField(max_length=500)
    tutor = models.CharField(max_length=500)
    moduls_repartits = models.DateField(max_length=500)