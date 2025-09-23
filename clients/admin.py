# clients/admin.py
from django.contrib import admin
from .models import Client, Task

# Register your models here.
admin.site.register(Client)
admin.site.register(Task)