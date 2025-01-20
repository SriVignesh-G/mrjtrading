from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UserData,Chart

# Create your views here.

def index_page(request):
    return render(request,'index.html')

def signup_login(request):
    if request.method == "POST":
        email = request.POST.get("email_id")
        pwd1 = request.POST.get("pwd1")
        pwd2 = request.POST.get("pwd2")
        user = UserData.objects.filter(email=email)
        if user:
            messages.error(request,'User Already Exists')
        elif pwd1 != pwd2:
            messages.error(request,'Password Doesn\'t match')
        else:
            UserData.objects.create(email=email,password=pwd1)
            return redirect('login')


    return render(request,'signup_login.html')

def viewCourse(request):
    return render(request,'course.html')

def login(request):
    email = request.POST.get("email_id")
    pwd = request.POST.get("pwd")
    user = UserData.objects.filter(email=email,password=pwd)
    if user:
        return redirect('chart',user[0].id)
    else:
         return render(request,'login.html')

def about(request):
    return render(request,'about.html')


def viewChart(request,id):
    user = UserData.objects.get(id=id)
    if user:
        charts = Chart.objects.all()
        context = {'charts':charts, 'user':user}
        return render(request,'charts.html',context)
    return redirect('login')

def blog(request,id):
    blog = Chart.objects.get(id=id)
    user = request.GET.get('user_id')
    print(user)
    context = {'blog':blog,'user':user}
    return render(request,'blog.html',context)