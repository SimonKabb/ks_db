from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('supplies.urls', namespace='supplies')),
    path('admin/', admin.site.urls),

]
