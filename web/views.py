from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from homework import forms as hf


@login_required
def home(request):
    form = hf.HomeworkForm()

    context = {
        'form': form,
    }
    return render(request, 'web/home.html', context)
