from django.shortcuts import render, redirect
from accounts.registration_form import RegistrationForm, ProfileRegisterForm
from .forms import InputForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    context ={} 
    context['form']= InputForm() 
    return render(request, 'accounts/home.html', context)

def register(request):
    if request.method =='POST':
        registration_form = RegistrationForm(request.POST)
        p_reg_form = ProfileRegisterForm(request.POST)
        if registration_form.is_valid and p_reg_form.is_valid():
            user = registration_form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
        return redirect('/accounts')
    else:
        registration_form = RegistrationForm()
        p_reg_form = ProfileRegisterForm()

        args = {
            'form': registration_form,
            'p_reg_form' : p_reg_form
        }
        return render(request, 'accounts/reg_form.html', args)
    