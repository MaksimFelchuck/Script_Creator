import subprocess

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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


def Run_script(request, script_id):
    if request.method == 'GET':
        user = script(script_name=script_id)
        file_create = open('Script/static/scripts/' + script_id, 'w')
        file_create.close()
        with open('Script/static/scripts/' + script_id, 'r+') as file:
            text = script.objects.get(script_name=script_id)
            text = text.script
            file.write(str(text))
            file.close()

        process = subprocess.Popen("python Script/static/scripts/"+script_id, stdout=subprocess.PIPE)
        data = process.communicate()
        history = History(host_script=user, active_user=request.user, code=str(data[0]), run_time=str(datetime.datetime.now())[:19])
        history.save()

        return redirect('/scripts/')

def Show_history(request):
    history = History.objects.all()
    context = {
        "history": history
    }
    return render(request, 'History.html', context)
