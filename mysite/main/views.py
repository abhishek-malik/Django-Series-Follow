from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your views here.
def homepage(request):
	return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials":Tutorial.objects.all})
'''
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
'''
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "First name")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )
   

def register(request):
	form = RegisterForm
	return render(request,"main/register.html",context={"form":form})

