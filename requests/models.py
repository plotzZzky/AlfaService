from django.db import models

from customers.models import Customer


class Request(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
