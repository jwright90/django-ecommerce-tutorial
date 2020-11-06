from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

class HomeView(ListView):
    model = Item
    template_name = "home.html"

def home(request):
    context = {
        'item': Item.objects.all()
    }

    return render(request, "home.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

def product(request):
    context = {
        'product' : Item.objects.all()
    }

    return render(request, "product.html", context)

def checkout(request):
    context = {

    }

    return render(request, "checkout.html", context)
