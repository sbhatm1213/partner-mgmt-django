from django.db import models


class Distributor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    monthly_usage = models.IntegerField(default=0)

    distributor = models.ForeignKey(
        Distributor,
        related_name="partners",
        on_delete=models.CASCADE
    )

    hubspot_company_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
