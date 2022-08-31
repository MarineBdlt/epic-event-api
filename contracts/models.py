from django.conf import settings
from django.db import models
from datetime import date


class Contract(models.Model):

    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="contract_client"
    )
    amount = models.IntegerField(null=True)
    title = models.CharField(null=True, blank=True, max_length=50)
    content = models.CharField(null=True, blank=True, max_length=1000)
    date = models.DateField(default=date.today)
    support_team = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        limit_choices_to={"groups__name": "support_team"},
        null=True,
        on_delete=models.SET_NULL,
    )

    RED = "RED", "Rédaction"
    CS = "CS", "En cours de signature"
    S = "S", "Signé"
    T = "T", "Terminé"
    STATUS_CHOICES = [RED, CS, S, T]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=RED)

    def __str__(self):
        for choice in [self.RED, self.CS, self.S, self.T]:
            if self.status == choice[0]:
                str_status = choice[1]
            else:
                str_status = self.RED[1]
        return f"{self.client.company_name.capitalize()} | {self.title} | {str_status}"
