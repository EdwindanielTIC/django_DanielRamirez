from django.forms import ModelForm
from django.shortcuts import render,redirect
from django import forms
from .models import Alumne,Professors

class AlumneForm(forms.ModelForm):
    class Meta:
          fields = '__all__'
          model = Alumne


class ProfessorsForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Professors