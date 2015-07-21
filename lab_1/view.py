from django.shortcuts import render_to_response
from django.db.models import Q
from models import *
from django import forms

def index(request):
    p = Publisher(name = 'Zhenya', surename = 'Orlov', city = 'Kiev')
    p.save()
    b=User(name = 'Zhenya', nikname = 'Zen', email = 'evgenyorlov1@gmail.com')
    b.save()
    users = User.objects.all() #Note .all()
    return render_to_response('index.html', {'users': users})


def search(request):
    #Search works only for word's part, not only for complete
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query) # contains - case sensitive, icontains case insensitive
        )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('search.html', {"query": query, "users": results})


def add(request):
    inf = User(name =request.GET.get('name', ''), nikname = request.GET.get('nikname', ''), email = '')
    inf.save()
    return render_to_response('add.html', {'request': request.GET.get('name', '')} )


def home(request):
    return render_to_response('home.html ')


def delete(request):

    query = request.GET.get()
    users = User.objects.all()
    return render_to_response('delete.html', {'users': users})