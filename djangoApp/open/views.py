from django.shortcuts import render

# Create your views here.
def openPage(request):
    return render(request, 'open.html')

def registerPage(request):
    return render(request, 'register.html')

def loginPage(request):
    return render(request, 'login.html')