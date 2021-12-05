from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import new
from django.urls import reverse
from .forms import newForm, CreateUserForm, update1
from .serializer import EmbedSerializer
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormMixin, UpdateView
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.template.loader import get_template

from django.urls import reverse_lazy
from django.forms import Textarea
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

import requests

# Create your views here.
import accounts
from .import services

def home(request):
    return render(request, 'accounts/index.html')

def update(request, pk):
    gh = new.objects.get(id=pk)
    form = update1()
    form = update1(request.POST or None, instance = gh)
    if form.is_valid():
        messages.success(request, 'You data has been updated succesfully.')
        form.save()
        return redirect('form_submitted')
    return render(request, 'accounts/update.html', {'form': form})

def form_submitted(request):
    return render(request, 'accounts/form_submitted.html')

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')        
            return redirect('register')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if new.objects.filter(user=request.user).exists():
                return redirect('form_submitted')
            else:
                return redirect('upload')
        else:
            messages.error(request, "Username, password or email is incorrect.")
            return redirect('register')
                 

    context = {}
    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def day_plan(request):
    return render(request, 'accounts/day_plan.html')

def day_plan(request):
    return render(request, 'accounts/day_plan1.html')

def day_plan2(request):
    return render(request, 'accounts/day_plan2.html')

def rec1(request):
    return render(request, 'accounts/rec.html')

def upload(request):
    model = new
    form = newForm()
    if request.method == 'POST':
        form = newForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            url = 'https://api.edamam.com/api/recipes/v2?type=public&q=recipes&app_id=f521ef6d&app_key=8119142429b59a19afb28f098f448a52&mealType=Breakfast&mealType=Dinner&mealType=Lunch' 
            health = form.cleaned_data['diet']
            params = {'health': health}
            r = requests.get(url)
            dish_list = services.get_dish('balanced')
            print(dish_list)
            #json = r.json()
            #serializer = EmbedSerializer(data=json)
            #if serializer.is_valid():
                #embed = serializer.save()
                #print(embed)
            form.save()
            return redirect('form_submitted')

    context = {'form':form}
    return render(request, 'accounts/form.html', context)

class days(AccessMixin, ListView):
    template_name = 'accounts/days.html'
    model = new
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # This will redirect to the login view
            return self.handle_no_permission()

        # Checks pass, let http method handlers process the request
        return super().dispatch(request, *args, **kwargs)


