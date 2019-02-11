import mimetypes
import os

import subprocess



from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
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

        directory = os.getcwd()
        directory = directory.replace('web','scripts')

        os.chdir(directory)
        file_create = open(script.script_name + '.py', 'w')
        file_create.close()

        with open(script.script_name + '.py', 'r+') as file:
            file.write(str(script.script))
            file.close()
        directory = directory.replace('Script_Creator\scripts', 'jobs')
        os.chdir(directory)
        os.mkdir(script.script_name)
        directory = directory.replace('jobs', 'Script_Creator\web')
        os.chdir(directory)

        script.save()


        return redirect('/scripts/')

    return render(request, 'form.html', context)


def Parameters(request, script_id):
    form = ParameterForm(request.POST or None)
    context = {
        'form': form,
        'script': script_id

    }
    if request.method == 'POST':
        form.save()
        return redirect('/scripts/')
    return render(request, 'parameter_form.html', context)
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
        index.script_format = request.POST.get('script_format')
        index.save()
        return redirect('/scripts/')

    return render(request, 'edit_form.html', context)


def Run_script(request, script_id):
    if request.method == 'GET':

        #user = script(script_name=script_id)
        #run_script = script.objects.get(script_name=script_id)
        #print(os.path.abspath(os.curdir))
        directory = os.getcwd()
        directory = directory.replace('Script_Creator\web', 'libs-ci\core')
        os.chdir(directory)
        subprocess.call('python startjob.py ' + script_id)
        directory = directory.replace('libs-ci\core', 'Script_Creator\web')
        os.chdir(directory)
        return redirect('/scripts/')
        """""""""
        os.chdir('jobs')
        os.chdir(script_id)
        time = str(datetime.datetime.now())[:19].replace(' ', '_')
        time = time.replace('-', '.')
        time = time.replace(':', '.')
        os.mkdir(time)
        os.chdir(time)
        file_create()
        process = subprocess.Popen('python ' + script_id + '.py', stdout=subprocess.PIPE, shell=True)
        data = process.communicate()
        code = process.poll()
        if code == 0:
            code = "Completed"
        else:
            code = 'Error'
        history = History(host_script=user, active_user=request.user, console_output=str(data[0]), status=code,
                          run_time=str(datetime.datetime.now())[:19])
        history.save()
        os.remove(script_id + '.py')
        os.chdir('..')
        os.chdir('..')
    
    """""""""



"""""""""
        elif run_script.script_format == 'shell':
            os.chdir('..')
            os.chdir('libs-ci')
            script_shell = str(run_script.script)
            script_parameter = str(run_script.parameter)
            file_create = open(script_id + '.bat', 'w')
            file_create.close()
            with open(script_id + '.bat', 'r+') as file:
                text = run_script.script
                file.write(str(text))
                file.close()
            os.chdir('..')
            os.chdir('jobs')
            os.chdir(script_id)
            time = str(datetime.datetime.now())[:19].replace(' ', '_')
            time = time.replace('-', '_')
            time = time.replace(':', '.')
            os.mkdir(time)
            os.chdir(time)

            process = subprocess.Popen(script_shell + ' ' + script_parameter, stdout=subprocess.PIPE, shell=True)
            data = process.communicate()
            code = process.poll()

            if code == 0:
                code = "Completed"
            else:
                code = 'Error'

            history = History(host_script=user, active_user=request.user, console_output=str(data[0]), status=code,
                              run_time=str(datetime.datetime.now())[:19])
            history.save()
            os.chdir('..')
            os.chdir('..')


        return redirect('/scripts/')




@login_required
def Show_history(request):
    history = History.objects.all()
    context = {
        "history": history
    }
    return render(request, 'History.html', context)
   




def Parameters_edit(request, script_id):
    if request.method == 'POST':
        index = script.objects.get(script_name=script_id)
        index.parameter = request.POST.get('parameter')
        index.save()

        return redirect('/scripts/run/' + script_id)
"""""""""