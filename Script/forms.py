from django import forms
from django.contrib.auth.models import User



from .models import *


class ScriptForm(forms.ModelForm):
    class Meta:
        model = script
        exclude = ['creator']


