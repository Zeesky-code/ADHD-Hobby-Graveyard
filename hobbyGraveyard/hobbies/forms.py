from django import forms
from django.forms import ModelForm

from .models import *


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'