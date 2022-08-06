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
    
class Contract(models.Model):

    client = models.ForeignKey("epicevent_app.Client", on_delete=models.CASCADE, related_name="contract_client")
    title = models.CharField(null=True, blank=True, max_length=50)
    content = models.CharField(null=True, blank=True, max_length=1000)
    
    RED = "REDACTION", "Rédaction"
    CS = "EN SIGNATURE", "En cours de signature"
    S = "SIGNE", "Signé"
    T = "TERMINE", "Terminé"
    STATUS_CHOICES = [RED, CS, S, T]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=RED)
    
    def __str__(self):
        return f'{self.client.company_name.capitalize()} - {self.title} ➡️ {self.status}'

class ContractAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contract, ContractAdmin)

class Event(models.Model):
    
    contract = models.ForeignKey("epicevent_app.Contract", on_delete=models.CASCADE, related_name="event_contract")
    client = models.ForeignKey("epicevent_app.Client", on_delete=models.CASCADE, related_name="event_client")
    title = models.CharField(null=True, blank=True, max_length=50)
    description = models.CharField(null=True, blank=True, max_length=1000)
    is_over = models.BooleanField(default=False)

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)
    
