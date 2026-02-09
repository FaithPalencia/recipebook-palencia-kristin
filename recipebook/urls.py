# project/urls.py
from django.contrib import admin
from django.urls import include, path

app_name = 'ledger'
urlpatterns = [
    path('', include('ledger.urls')),
    path('admin/', admin.site.urls),
]