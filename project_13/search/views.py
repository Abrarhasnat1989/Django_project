from django.shortcuts import render
from .models import Item

def search(request):
    query = request.GET.get('q')
    items = Item.objects.filter(name__icontains=query)
    return render(request, 'search/results.html', {'items': items, 'query': query})
