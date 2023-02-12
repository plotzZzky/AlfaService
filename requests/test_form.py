from django.test import TestCase

from .forms import RequestForm
from customers.models import Customer


class RequestFormTest(TestCase):
    def create_customer(self):
        customer = Customer(
            cpf='123.123.123-12',
            name='name',
            lastname='lastname',
            address='address',
            city='city',
            telephone='(11)909090',
            email='name@mail.com',
        )
        customer.save()
        return customer
