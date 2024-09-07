from django.shortcuts import render,HttpResponse,redirect
def dashboard(request):
    return render(request,"authh/login.html",{})