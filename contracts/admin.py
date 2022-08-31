from django.contrib import admin
from contracts.models import Contract


class ContractAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contract, ContractAdmin)
