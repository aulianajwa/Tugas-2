from ast import If
from http.client import HTTPResponse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from todolist.forms import Task_Form
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request) :
    data_list = Task.objects.filter(user=request.user)
    context = {
        'list_todo' : data_list,
        'username' : request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request) :
    form = Task_Form(request.POST or None)
    if request.method == 'POST' :
        if form.is_valid() :
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todolist')
    
    context = {'forms' : form}
    return render(request,'create_task.html',context)

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def toggle_task(request,id) :
    task = Task.objects.get(id=id)
    if task.is_finished :
        task.is_finished = False
    else :
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

def show_json(request) :
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task(request) :
    form = Task_Form(request.POST or None)
    if request.method == 'POST' :
        if form.is_valid() :
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            task = Task.objects.create(user = request.user, date=datetime.date.today(),title=title, description=description)
            data = {
                "pk": task.pk,
                "title": task.title,
                "description": task.title,
                "is_finished": task.is_finished,
                "date": task.date
            }
            task.save()
        return JsonResponse(data)