from django.db import models


class Quota(models.Model):
    currency = models.CharField(max_length=60, blank=False, default='')


