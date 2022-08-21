from django.forms import ModelForm
from django import forms
from .models import *



class TumerDetectionForm(ModelForm):
    class Meta:
        model = DetectionImage
        fields = '__all__'
        