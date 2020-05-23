from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm


@login_required
def register_user(request):
    if request.user.first_name:
        return redirect('/')
    form = UserForm(request.POST or None, instance = request.user)
    if request.method == 'POST':
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)