from django.shortcuts import render_to_response
from django.db.models import Q
from models import *

def view1(request):
    p=Publisher(name='Zhenya', surename='Orlov', city='Kiev')
    p.save()
    b=User(name='Zhenya', nikname='Zen', email='evgenyorlov1@gmail.com')
    b.save()
    return render_to_response('index.html', {'name': p.name, 'email': b.email})

def form(request):
    query=request.GET.get('q', '')
    if query:
        qset=(
            Q(name__icontains=query)
        )
        results=Publisher.objects.filter(qset).distinct()
    else:
        results=[]
    return render_to_response('search.html', {"query": query, "results": results})
