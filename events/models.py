from django.db import models
from django.contrib import admin


class Event(models.Model):
    
    contract = models.ForeignKey("contracts.Contract", on_delete=models.CASCADE, related_name="event_contract")
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="event_client")
    title = models.CharField(null=True, blank=True, max_length=50)
    description = models.CharField(null=True, blank=True, max_length=1000)
    is_over = models.BooleanField(default=False)

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)
    

# Create your models here.
