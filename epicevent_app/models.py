from django.db import models

class Client(models.Model):

    client_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    company_name = models.CharField(50, null=False)
    date_created = models.IntegerField()
    sales_contact = models.IntegerField()
    contract = models.ForeignKey("epicevent_app.Contract", on_delete=models.CASCADE, related_name="contract")
    
    def __str__(self):
        return str(self.client_id, self.first_name, self.last_name, self.email)
    
class Contract(models.Model):
    
    contract_id = models.IntegerField()
    client = models.ForeignKey("epicevent_app.Client", on_delete=models.CASCADE, related_name="client")
    title = models.CharField(max_length=50)
    content = models.CharField()

class Contract_Status(models.Model):
    
    contract_status_id = models.IntegerField()
    contract = models.ForeignKey("epicevent_app.Contract", on_delete=models.CASCADE, related_name="contract")
    is_signed = models.BooleanField(default=False)

class Event(models.Model):
    
    event_id = models.IntegerField()
    contract = models.ForeignKey("epicevent_app.Contract", on_delete=models.CASCADE, related_name="contract")
    client = models.ForeignKey("epicevent_app.Client", on_delete=models.CASCADE, related_name="client")
    title = models.CharField(max_length=50)
    description = models.CharField()
    is_over = models.BooleanField(default=False)
    
    
    

    # project_id = models.ForeignKey(
    #     "softdesk_api.Project", on_delete=models.CASCADE, related_name="project"
    # )

# class ContributorAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Contributor, ContributorAdmin)

# Create your models here.
