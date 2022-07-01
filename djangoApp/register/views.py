from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def login(request):
    user = User.objects.create_user(username = request.GET['username'], email = request.GET['email'], password = request.GET['password'])
    return render(request, 'login.html')