from django.contrib import admin
from .models import Client,Invoice,Product,Settings

# Register your models here.


admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Settings)