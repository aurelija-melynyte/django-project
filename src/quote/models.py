from django.db import models


class Quote(models.Model):
    currency = models.CharField(max_length=60, blank=False, default='')


