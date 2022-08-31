from django.contrib import admin
from clients.models import Client


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
