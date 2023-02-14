from django.test import TestCase
from django.contrib.auth.models import User

from customers.models import Customer
from customers.forms import CustomerForm


class CustomersTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'temporary',
            'password': 'temporary'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_get_table_status(self):
        response = self.client.get("/customers/table/")
        self.assertEqual(response.status_code, 302)

    def test_get_table_logged_status(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/customers/table/")
        self.assertEqual(response.status_code, 200)

    def test_get_table_template(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/customers/table/")
        self.assertTemplateUsed(response, "customers_table.html")

    def test_get_form_logged_status(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/customers/form/")
        self.assertEqual(response.status_code, 200)

    def test_get_form_logged_template(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/customers/form/")
        self.assertTemplateUsed(response, "new_customer.html")

    def create_new_customer(self):
        self.client.login(username='temporary', password='temporary')
        data = {
            'cpf': '11111111111',
            'name': 'temporary',
            'lastname': 'temporary',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        response = self.client.post("/customers/new/", data)
        return response

    def test_create_customer_status(self):
        response = self.create_new_customer()
        self.assertEqual(response.status_code, 200)

    def test_create_customer_content(self):
        response = self.create_new_customer()
        model = Customer.objects.get(name='temporary')  # type:ignore
        self.assertEqual(model.name, 'temporary')

    def test_delete_customer_status(self):
        self.create_new_customer()
        model = Customer.objects.get(name='temporary')  # type:ignore
        response = self.client.get(f"/customers/delete/id={model.id}/")
        self.assertEqual(response.status_code, 200)

    def test_delete_customer_status_404(self):
        self.create_new_customer()
        response = self.client.get(f"/customers/delete/id=/")
        self.assertEqual(response.status_code, 404)

    def test_delete_customer_result(self):
        self.create_new_customer()
        model = Customer.objects.get(name='temporary')  # type:ignore
        response = self.client.get(f"/customers/delete/id={model.id}/")
        try:
            result = Customer.objects.get(name='temporary')  # type:ignore
        except Customer.DoesNotExist:  # type:ignore
            result = False
        self.assertFalse(result)

    def test_get_edit_customer_status(self):
        self.create_new_customer()
        model = Customer.objects.get(name='temporary')  # type:ignore
        response = self.client.get(f"/customers/edit={model.id}/")
        self.assertEqual(response.status_code, 200)

    def test_post_edit_customer_status(self):
        self.create_new_customer()
        model = Customer.objects.get(name='temporary')  # type:ignore
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        response = self.client.post(f"/customers/edit={model.id}/", data)
        self.assertEqual(response.status_code, 202)

    def test_edit_customer_result(self):
        self.create_new_customer()
        model = Customer.objects.get(name='temporary')  # type:ignore
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        response = self.client.post(f"/customers/edit={model.id}/", data)
        result = Customer.objects.get(name='temporary1')  # type:ignore
        self.assertEqual(result.name, data['name'])

    def test_edit_customer_status_404(self):
        self.create_new_customer()
        response = self.client.post(f"/customers/edit=/")
        self.assertEqual(response.status_code, 404)


class ModelTest(TestCase):
    def setUp(self):
        pass

    def test_create_model_success(self):
        model = Customer(
            cpf=111111111,
            name='temporary',
            lastname='temporary',
            address='temporary',
            city='temporary',
            telephone='(11)11111111',
            email='temporary@mail.com'
        )
        model.save()
        result = Customer.objects.get(name='temporary')  # type:ignore
        self.assertEqual(result.name, 'temporary')

    def test_create_model_no_email(self):
        model = Customer(
            cpf=111111111,
            name='temporary',
            lastname='temporary',
            address='temporary',
            city='temporary',
            telephone='(11)11111111',
        )
        model.save()
        result = Customer.objects.get(name='temporary')  # type:ignore
        self.assertEqual(result.name, 'temporary')


class FormTest(TestCase):
    def setUp(self):
        pass

    def test_form_sucess(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_cpf_empty_error(self):
        data = {
            'cpf': '',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_name_empty_error(self):
        data = {
            'cpf': '11111111111',
            'name': '',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_lastname_empty_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': '',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_address_empty_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': '',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_city_empty_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': '',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_telephone_empty_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_cpf_min_11_error(self):
        data = {
            'cpf': '1111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_name_min_4_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'aaa',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_lastname_min_4_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'aaa',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_address_min_10_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'aaaaaaaaa',
            'city': 'temporary',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_city_min_3_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'aa',
            'telephone': '(11)00000000',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_telephone_min_12_error(self):
        data = {
            'cpf': '11111111111',
            'name': 'temporary1',
            'lastname': 'temporary1',
            'address': 'rua qualquer, 000',
            'city': 'temporary',
            'telephone': '(51)111111',
            'email': 'temporary@mail.com'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
