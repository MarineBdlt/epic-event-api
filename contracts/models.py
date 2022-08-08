from django.db import models
from django.contrib import admin

class Contract(models.Model):

    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="contract_client")
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
