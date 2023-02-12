from django.test import TestCase

from .forms import CustomerForm
from .models import Customer


class CustomerFormTest(TestCase):
    def test_customer_empty_cpf(self):
        data = {'cpf': '',
                'name': 'name',
                'lastname': 'lastname',
                'address': 'address',
                'city': 'city',
                'telephone': '(11)90909090',
                'email': 'email', }
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertFalse(result)

    def test_customer_empty_name(self):
        data = {'cpf': '123.123.123-12',
                'name': '',
                'lastname': 'lastname',
                'address': 'address',
                'city': 'city',
                'telephone': '(11)90909090',
                'email': 'email', }
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertFalse(result)

    def test_customer_empty_lastname(self):
        data = {'cpf': '123.123.123-12',
                'name': 'name',
                'lastname': '',
                'address': 'address',
                'city': 'city',
                'telephone': '(11)90909090',
                'email': 'email', }
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertFalse(result)

    def test_customer_empty_address(self):
        data = {'cpf': '123.123.123-12',
                'name': 'name',
                'lastname': 'lastname',
                'address': '',
                'city': 'city',
                'telephone': '(11)90909090',
                'email': 'email', }
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertFalse(result)

    def test_customer_empty_city(self):
        data = {'cpf': '123.123.123-12',
                'name': 'name',
                'lastname': 'lastname',
                'address': 'address',
                'city': '',
                'telephone': '(11)90909090',
                'email': 'email', }
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertFalse(result)

    def test_customer_empty_telephone(self):
        data = {'cpf': '123.123.123-12',
                'name': 'name',
                'lastname': 'lastname',
                'address': 'address',
                'city': 'city',
                'telephone': '',
                'email': 'email', }
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertFalse(result)

    def test_customer_empty_email(self):
        data = {'cpf': '123.123.123-12',
                'name': 'name',
                'lastname': 'lastname',
                'address': 'address',
                'city': 'city',
                'telephone': '(11)90909090',
                'email': ''}
        customer = CustomerForm(data)
        result = customer.is_valid()
        self.assertTrue(result)


class CustomerTest(TestCase):
    def test_customer_create(self):
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
        result = Customer.objects.get(pk=customer.id)
        self.assertTrue(result)

