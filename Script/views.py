import mimetypes
import os

import subprocess
import zipfile
from wsgiref.util import FileWrapper

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
        run_script = script.objects.get(script_name=script_id)

        if run_script.script_format == '.py':
            file_create = open('Script/static/scripts/' + script_id + '.py', 'w')
            file_create.close()
            with open('Script/static/scripts/' + script_id + '.py', 'r+') as file:
                text = run_script.script
                file.write(str(text))
                file.close()
                process = subprocess.Popen("python Script/static/scripts/" + script_id + '.py', stdout=subprocess.PIPE)
                data = process.communicate()
                data = data[0].decode("utf-8")

                history = History(host_script=user, active_user=request.user, code=str(data),
                                  run_time=str(datetime.datetime.now())[:19])
                history.save()
        elif run_script.script_format == 'shell':

            process = subprocess.Popen(script_id, stdout=subprocess.PIPE)
            data = process.communicate()
            data = data[0].decode("utf-8")
            history = History(host_script=user, active_user=request.user, code=str(data),
                              run_time=str(datetime.datetime.now())[:19])
            history.save()

        return redirect('/scripts/')


@login_required
def Show_history(request):
    history = History.objects.all()
    context = {
        "history": history
    }
    return render(request, 'History.html', context)


def git_clone(request):
    form = Script_from_git_Form(request.POST or None)
    files = Script_from_github.objects.all()
    context = {
        'form': form,
        'files': files
    }
    if request.method == 'POST' and form.is_valid():
        git = form.save(commit=False)

        subprocess.call('git clone ' + git.link)
        git_name = git.link
        git_name = git_name.replace('https://github.com/','')
        git_name = git_name.replace('/', '_')
        git_name = git_name.replace('.git', '')
        creator_name =''
        for i in git_name:
            if i != '_':
                creator_name += i
            else:
                creator_name += i
                break

        git_name =git_name.replace(creator_name,'')

        z = zipfile.ZipFile('Script/static/git files/'+git_name+'.zip', 'w')

        for root, dirs, files in os.walk(git_name):
            for file in files:
                z.write(os.path.join(root, file))
        z.close()
        file = open('Script/static/git files/' + git_name+'.zip', 'rb')
        django_file = File(file)
        git.link = git_name+'.zip'
        git.zip_file.save('Script/static/git files/'+git_name+'.zip', django_file, save=True)


        return redirect('/scripts/')

    return render(request, 'git.html', context)


def download_file(request, file):
    directory = 'Script/static/git files/'
    the_file = directory + file
    filename = os.path.basename(the_file)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                                     content_type=mimetypes.guess_type(the_file)[0])
    response['Content-Length'] = os.path.getsize(the_file)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


