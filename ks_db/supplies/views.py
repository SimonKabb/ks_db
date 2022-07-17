from django.shortcuts import render
from .models import Ks_db
from .cbr import dollar_rate
from .shets import read_table
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'cred.json')


def index(request):
    orders = Ks_db.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'supplies/index.html', context)


def refresh_db(request):
    spreadsheet_id = '1gmOeYU2Z-UL5RAfBxNgaecCfjMdM9bvLi5knCqVqNjs'
    sheet_data = read_table(spreadsheet_id, CREDENTIALS_FILE)
    dollar_cource = dollar_rate()
    for data in sheet_data[1:]:
        date = datetime.strptime(data[3], '%d.%m.%Y')
        old_row = get_object_or_404(Ks_db, id=data[0])
        try:
            Ks_db.objects.get(id=data[0])
            old_row.ord = data[1]
            old_row.price = data[2]
            old_row.rub = int(data[2])*dollar_cource
            old_row.delivery_time = date
            old_row.save()
        except Ks_db.DoesNotExist:
            new = Ks_db.objects.create(id=data[0],
                                       ord=data[1],
                                       price=data[2],
                                       rub=int(data[2])*dollar_cource,
                                       delivery_time=date)
    return redirect('supplies:index')
