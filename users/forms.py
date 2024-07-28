from django import forms
from .models import UserModel, ProfileModel
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator



class ProfileForm(forms.ModelForm):
    # zip_code = forms.IntegerField(validators=[MaxLengthValidator(6)])
    
    class Meta:
        model = ProfileModel
        exclude = ['user', 'created_at']
        widgets = {
            'adress' : forms.TextInput(attrs={
                'placeholder' : 'Street Adress'
            }),
            'adress_2' : forms.TextInput(attrs={
                'placeholder' : 'Apartment, suit '
            }),
        }




class LoginForm(forms.Form):
    username  = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : 'Username'
    }), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input100',
        'placeholder' : 'Password'
    }), label=False)





class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input100',
        'placeholder' : 'Username'
    }), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input100',
        'placeholder' : 'Password'
    }),label=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input100',
        'placeholder' : 'Confirm Password'
    }),label=False)


    

    def clean_username(self):
        username = self.cleaned_data['username']
        user = UserModel.objects.get(username=username)
        if user:
           raise ValidationError(f'Ushbu {username} nomli username band!')
        return self.cleaned_data['username']
    
    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar bir xil emas')
        return self.cleaned_data['confirm_password']

