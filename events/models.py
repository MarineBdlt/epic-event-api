from django.db import models
from django.contrib import admin


class Event(models.Model):
    
    contract = models.ForeignKey("contracts.Contract", on_delete=models.CASCADE, related_name="event_contract")
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="event_client")
    title = models.CharField(null=True, blank=True, max_length=50)
    description = models.CharField(null=True, blank=True, max_length=1000)
    is_over = models.BooleanField(default=False)
    
    def __str__(self):
        if self.is_over == False:
            status = "En cours"
        else:
            status = "Terminé"
        return f'{self.client.company_name.capitalize()} | {self.contract.title} | {status}'

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)
    
