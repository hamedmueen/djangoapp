from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import os.path, json, time, os
from threading import *
# Create your views here.
orderTimer = None

order_id = 1

def timer(t):
    global orderTimer
    while t:
        mins = t // 60
        secs = t % 60
        orderTimer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1

def cart(request):
    global order_id
    if os.path.exists('./json/'+request.user.get_username()+'_cart.json'):
        with open('./json/'+request.user.get_username()+'_cart.json','r') as f:
            json_file = json.load(f)
            items = json_file['orders']
            total = 0
            for item in items:
                total = total + item['price']
            f.close()
        return render(request, 'cart.html', {'items': items, 'total': total, 'id': order_id })
    else:
        return HttpResponse('No orders')

def orderpage(request):
    global orderTimer
    t = Thread(target=timer, args=[30])
    t.start()
    print('dsd')
    global order_id
    order_id +=1
    return HttpResponseRedirect(redirect_to='/order')

def order(request):
    global orderTimer
    global order_id
    order_id += 1
    with open('./json/'+request.user.get_username()+'_cart.json', 'r') as f:
        cart_json = json.load(f)
        total = 0
        names = []
        for item in cart_json['orders']:
            names.append(item['name'])
            total += item['price']
        f.close()
    if os.path.exists('./json/'+request.user.get_username()+'_orders.json'):
        with open('./json/'+request.user.get_username()+'_orders.json','r+') as f:
            orders_json = json.load(f)
            orders_json['orders'].append({'id':order_id, 'items': names, 'cost': total})
            f.seek(0)
            json.dump(orders_json, f, indent=4)
            f.close()
    else:
        with open('./json/' + request.user.get_username() + '_orders.json', 'w') as f:
            json.dump({"orders": [{'id': order_id,'items': names, 'cost':total}]}, f, indent = 4)
            f.close()
    os.remove('./json/'+request.user.get_username()+'_cart.json')
    return render(request, 'order.html', {'order': {'id':order_id, 'items': names, 'cost': total}, 'orderTimer': orderTimer})

def backhome(request):
    return HttpResponseRedirect(redirect_to='/home')