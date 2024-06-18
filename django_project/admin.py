# gym/admin.py
from django.contrib import admin
from .models import Trainer, Class, Payment

admin.site.register(Trainer)
admin.site.register(Class)
admin.site.register(Payment)
