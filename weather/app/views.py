import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from .decorators import login_required
from .forms import UserForm, LoginForm
from .models import User


def UserView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    template = 'userlogin.html'
    context = {'form':form}
    return render(request,template,context)


def login(request):
    form = LoginForm
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email,password=password)
            if user:
                request.session['email']=email
                return redirect('/w')
    template = 'userlogin.html'
    context = {'form': form,'a':'login'}
    return render(request, template, context)


@method_decorator(login_required, name='dispatch')
class Weather(View):
    def get(self,request):
        template='weather.html'
        return render(request,template)

    def post(self,request):
        try:
            c=request.POST['name']
            city=c.title()
            apikey=''
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid='+apikey
            url = api_address + city
            json_data = requests.get(url).json()

            description=json_data['weather'][0]['description']
            icon=json_data['weather'][0]['icon']
            tempreture=json_data['main']['temp']-273
            temp="%.2f"%tempreture
            pressure=json_data['main']['pressure']
            humidity=json_data['main']['humidity']

            dict={
                'city': city,
                'description': description,
                'icon': icon,
                'temp': temp,
                'pressure': pressure,
                'humidity': humidity
            }

            template = 'weather.html'
            context={'dict':dict}
            return render(request, template,context)
        except:
            message=json_data['message']
            print(message)
            template = 'apicall/weather.html'
            context = {'error': message}
            return render(request, template, context)
