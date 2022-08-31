from django.db import models
from datetime import date
from django.conf import settings


class Client(models.Model):

    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    mobile = models.CharField(blank=True, null=True, max_length=10)
    phone = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(null=True)
    company_name = models.CharField(max_length=50, null=False)
    date_created = models.DateField(default=date.today)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        limit_choices_to={"groups__name": "sales_team"},
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.company_name.capitalize()
