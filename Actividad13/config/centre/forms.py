from django.forms import ModelForm
from django.shortcuts import render,redirect
from django import forms
from .models import Alumne

class AlumneForm(forms.ModelForm):
    class Meta:
          fields = '__all__'
          model = Alumne


        