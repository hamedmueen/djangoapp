from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import food
from datetime import datetime
import os.path
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
counter = 0

def failedlogin(request):
    return render(request, 'failedlogin.html')

def backtologin(request):
    return HttpResponseRedirect(redirect_to='/login')

def home(request):
    global counter
    foods = food.objects.all()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html', {'counter': counter, 'foods': foods, 'username': username})
        else:
            return HttpResponseRedirect(redirect_to='/failedlogin')
    else:
        if request.user.is_authenticated:
            foods = food.objects.all()
            return render(request, 'home.html', {'counter': counter, 'foods': foods, 'username': request.user.get_username()})

def addtocart(request, id):
    global counter
    obj = food.objects.get(id=id)
    time = datetime.now()
    item = {'username': 'test', 'name': obj.name,'price': obj.price,'time': time}
    if os.path.exists('./json/'+request.user.get_username()+'_cart.json'):
        with open('./json/'+request.user.get_username()+'_cart.json','r+') as f:
            orders = json.load(f)
            orders['orders'].append(item)
            f.seek(0)
            json.dump(orders, f, cls=DjangoJSONEncoder, indent=4)
            f.close()
    else:
        with open('./json/'+request.user.get_username()+'_cart.json','w') as f:
            json.dump({'orders':[item]}, f, cls=DjangoJSONEncoder, indent=4)
            f.close()
    counter += 1
    return HttpResponseRedirect(redirect_to='/home')

def signout(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')

def backhome(request):
    return HttpResponseRedirect(redirect_to='/home')

def removeitem(request, name):
    global counter
    counter -= 1
    with open('./json/'+request.user.get_username()+'_cart.json','r') as f:
        orders = json.load(f)['orders']
        for order in orders:
            if order['name'] == name:
                orders.remove(order)
                break
        f.close()
    with open('./json/' + request.user.get_username() + '_cart.json', 'w') as f:
        json.dump({'orders': orders}, f, indent=4)
        f.close()
    return HttpResponseRedirect(redirect_to='/cart')