from django.db import models


class Customer(models.Model):

    cpf = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
