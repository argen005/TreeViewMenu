from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def menu_view(request):
    menu_items = MenuItem.objects.filter(parent=None).distinct()
    return render(request, 'index.html', {'menu_items': menu_items})

def menu_item_detail(request, slug):
    item = get_object_or_404(MenuItem, slug=slug)
    return render(request, 'menu_item_detail.html', {'item': item})
