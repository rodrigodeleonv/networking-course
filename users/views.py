from django.shortcuts import render, redirect
from users import forms as uf


def register(request):
    if request.method == 'POST':
        form = uf.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = uf.UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
