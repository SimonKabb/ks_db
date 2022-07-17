from django.shortcuts import render
from .models import Ks_db


def index(request):
    orders = Ks_db.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'supplies/index.html', context)
