from django.db import models
from django.contrib import admin
from datetime import date

class Client(models.Model):

    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    mobile = models.CharField(blank=True, null=True, max_length=10)
    phone = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(null=True)
    company_name = models.CharField(max_length=50, null=False)
    date_created = models.DateField(default=date.today)
    sales_contact = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name.capitalize()

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)
