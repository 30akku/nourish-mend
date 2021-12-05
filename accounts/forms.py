from django.forms import ModelForm
from .models import new
from django.forms import Textarea, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import FileInput

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        widgets = {
            "username": TextInput(attrs={"placeholder": "Username"}),
            "first_name": TextInput(attrs={"placeholder": "First Name"}),
            "last_name": TextInput(attrs={"placeholder": "Last Name"}),
            "email": EmailInput(attrs={"placeholder": "Email"}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password'})


class DateInput(forms.DateInput):
    input_type = 'date'
    
class newForm(ModelForm):
    class Meta:
        model = new
        fields = ["fname", "weight","height", "diet", "age", "gender1", "disorder"]
    
        widgets = {
            "fname": TextInput(attrs={"placeholder": "Full name",}),
            #"dob": TextInput(attrs={"placeholder": "mm/dd/yyyy",}),
            'gender': forms.Select(attrs={'class': 'custom-select md-form'}),
            #'dob': DateInput(),
            'diet': forms.Select(attrs={'class': 'custom-select md-form'}),
            'disorder': forms.Select(attrs={'class': 'custom-select md-form'}),
        }

class update1(ModelForm):
    class Meta:
        model = new
        fields = ["fname", "weight","height", "diet", "age", "gender1", "disorder"]