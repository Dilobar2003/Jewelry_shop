from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ValidationError
from django.views.generic import  FormView, TemplateView, UpdateView
from .forms import RegistrationForm, LoginForm, ProfileForm
from .models import UserModel, ProfileModel
from django.contrib.auth import login, logout, authenticate





class UserProfileView(UpdateView):
    template_name = 'main/profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse('users:profile')

    def get_object(self, queryset=None):
        profile, created = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile
    

 


    





def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if not user is None:
                login(request, user)
                return redirect('main:home')
            form.add_error('password', 'wrong......')
    return render(request, 'login/login.html', context={
        
        'form' : form
    })    



def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = UserModel(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
        return redirect('users:login')
    
    return render(request, 'login/register.html', context={
        'registration_form' : form
  
    })



def logout_view(request):
    logout(request)
    return redirect('users:login')





