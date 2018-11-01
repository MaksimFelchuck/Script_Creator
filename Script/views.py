from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/"

    template_name = "register.html"

    def form_valid(self, form):

        form.save()

        return super(RegisterFormView, self).form_valid(form)


def Home(request):
    return render(request, 'home.html')


@login_required
def Script(request):
    form = ScriptForm(request.POST or None)
    #
    context = {'form': form,
               'date': str(datetime.datetime.now())[:10],
               #
               }

    if request.method == 'POST' and form.is_valid():
        script = form.save(commit=False)
        script.creator = request.user
        script.save()
        return redirect('/scripts/')

    return render(request, 'form.html', context)


@login_required
def Scripts(request):
    elements = script.objects.all()
    context = {
        'Scripts': elements
    }

    return render(request, 'Scripts.html', context)


def Delete_script(request, script_id):
    if request.method == 'GET':
        index = script.objects.get(script_name=script_id)
        index.delete()
        return redirect('/scripts/')


def Edit(request, script_id):
    index = script.objects.get(script_name=script_id)
    text = index.script
    context = {
        'index': index,
        'text': text,
        'date': str(datetime.datetime.now())[:10]
    }
    if request.method == 'POST':
        index.script = request.POST.get('script')
        index.save()
        return redirect('/scripts/')

    return render(request, 'edit_form.html', context)


def Registration(request):
    form = RegisterFormView(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        # user = User.objects.create_user(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['password'])
        return redirect('/scripts/')
    return render(request, 'register.html', context)
