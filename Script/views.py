from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .forms import *
from .models import *


# Create your views here.

def Home(request):
    return render(request, 'home.html')


@login_required
def Script(request):
    form = ScriptForm(request.POST or None)

    context = {'form': form,
               'date': str(datetime.datetime.now())[:10],

               }

    if request.method == 'POST' and form.is_valid():
        form.save()
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


