from django.db import models
from django.contrib import admin

class Contract(models.Model):

    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="contract_client")
    title = models.CharField(null=True, blank=True, max_length=50)
    content = models.CharField(null=True, blank=True, max_length=1000)
    
    RED = '1', 'Rédaction'
    CS = '2', 'En cours de signature'
    S = '3', 'Signé'
    T = '4', 'Terminé'
    STATUS_CHOICES = [RED, CS, S, T]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=RED)
    
    def __str__(self):
        for choice in [self.RED, self.CS, self.S, self.T]:
            if self.status == choice[0]:
                str_status = choice[1]
        return f'{self.client.company_name.capitalize()} | {self.title} | {str_status}'

class ContractAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contract, ContractAdmin)
