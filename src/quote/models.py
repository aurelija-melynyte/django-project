from django.db import models


class Quote(models.Model):
    base_currency = models.CharField(blank=False, default="", max_length=3)
    quote_currency = models.CharField(blank=False, default="", max_length=3)
    base_amount = models.IntegerField(blank=False, default=0)
    calculated_amount = models.FloatField(blank=False, default=0)
