from django import forms
from .models import *


class ScriptForm(forms.ModelForm):
    class Meta:
        model = script
        exclude = ['creator', 'create_date']


class Script_from_git_Form(forms.ModelForm):
    class Meta:
        model = Script_from_github
        exclude = ['zip_file']
