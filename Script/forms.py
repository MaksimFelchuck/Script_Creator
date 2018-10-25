from django import forms
from .models import *


class ScriptForm(forms.ModelForm):
    class Meta:
        model = script
        exclude = [""]

