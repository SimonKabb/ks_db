from django.urls import path
from . import views
app_name = 'supplies'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('refresh_db',
         views.refresh_db, name='refresh_db'),
]
