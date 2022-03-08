from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=60)
    ancient_name = models.CharField(max_length=60)
    # The __str__() method tells Django which information to show when it refers to individual entries
    def __str__(self):
        return self.name
