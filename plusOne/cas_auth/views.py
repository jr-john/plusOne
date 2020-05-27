from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm
import re
from django.contrib import messages


# @login_required
def register_user(request):
    # if request.user.first_name:
    #    return redirect('/')
    form = UserForm(request.POST or None, instance = request.user)
    if request.method == 'POST':
        if form.is_valid():
            temp_list=form.cleaned_data
            temp_num=temp_list.get('last_name')
            temp_email=temp_list.get('email')
            x=re.findall("[0-9]", temp_num)
            if len(x) == 10 :
                form.save()
                return redirect('/')
            else:
                messages.info(request, 'Enter Valid Phone Number')
                return render(request, 'register.html', {'form' : form})
        else:
            messages.info(request, 'Enter Valid Email Address')
            return render(request, 'register.html', {'form' : form})        
    context = {
        'form': form
    }
    return render(request, 'register.html', context)