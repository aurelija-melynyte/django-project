from django.contrib import admin
from .models import Cat

"""
Django includes some models in the admin site automatically, such as User and Group,
but the models we create need to be added manually.
"""

admin.site.register(Cat)
