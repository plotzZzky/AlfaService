from django.test import TestCase
from django.contrib.auth.models import User

from .models import Request
from customers.models import Customer


class RequestsTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'temporary',
            'password': 'temporary'
        }
        self.user = User.objects.create_user(**self.credentials)

    def create_new_customer(self):
        self.client.login(username='temporary', password='temporary')
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
        return result

    def create_new_requests(self):
        customer = self.create_new_customer()
        request = Request(customer=customer, title='temporary1', order='temporary1', status=2)
        request.save()
        return request

    def test_get_table_status(self):
        response = self.client.get("/requests/table/")
        self.assertEqual(response.status_code, 302)

    def test_get_table_logged_status(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/requests/table/")
        self.assertEqual(response.status_code, 200)

    def test_get_table_template(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/requests/table/")
        self.assertTemplateUsed(response, "requests_table.html")

    def test_get_form_logged_status(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/requests/form/")
        self.assertEqual(response.status_code, 200)

    def test_get_form_logged_template(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/requests/form/")
        self.assertTemplateUsed(response, "new_request.html")

    def test_create_request_status(self):
        customer = self.create_new_customer()
        data = {
            'choice': customer.id,
            'title': 'temporary',
            'order': 'temporary',
            'status': '2'
        }
        response = self.client.post("/requests/new/", data)
        self.assertEqual(response.status_code, 201)

    def test_create_request_result(self):
        customer = self.create_new_customer()
        data = {
            'choice': customer.id,
            'title': 'temporary',
            'order': 'temporary',
            'status': '2'
        }
        self.client.post("/requests/new/", data)
        result = Request.objects.get(title='temporary')  # type:ignore
        self.assertEqual(data['title'], result.title)

    def test_delete_request_status(self):
        self.client.login(username='temporary', password='temporary')
        request = self.create_new_requests()
        response = self.client.get(f"/requests/delete/id={request.id}/")  # type:ignore
        self.assertEqual(response.status_code, 200)

    def test_delete_request_content(self):
        self.client.login(username='temporary', password='temporary')
        request = self.create_new_requests()
        self.client.get(f"/requests/delete/id={request.id}/")  # type:ignore
        try:
            result = Request.objects.get(pk=request.id)  # type:ignore
        except Request.DoesNotExist:  # type:ignore
            result = None
        self.assertIsNone(result)

    def test_delete_request_status_error(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(f"/requests/delete/id=90/")  # type:ignore
        self.assertEqual(response.status_code, 500)

    def test_delete_request_id_empty_status_error(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(f"/requests/delete/id=/")  # type:ignore
        self.assertEqual(response.status_code, 404)

    def test_get_edit_requests_status(self):
        self.client.login(username='temporary', password='temporary')
        request = self.create_new_requests()
        response = self.client.get(f"/requests/edit={request.id}/")  # type:ignore
        self.assertEqual(response.status_code, 200)

    def test_get_edit_requests_edit_status(self):
        self.client.login(username='temporary', password='temporary')
        customer = self.create_new_customer()
        request = Request(customer=customer, title='temporary1', order='temporary1', status=2)
        request.save()
        data = {
            'choice': customer.id,
            'title': 'temporary',
            'order': 'temporary',
            'status': '2'
        }
        response = self.client.post(f"/requests/edit={request.id}/", data)  # type:ignore
        self.assertEqual(response.status_code, 200)

    def test_get_edit_requests_edit_content(self):
        self.client.login(username='temporary', password='temporary')
        customer = self.create_new_customer()
        request = Request(customer=customer, title='temporary1', order='temporary1', status=2)
        request.save()
        data = {
            'choice': customer.id,
            'title': 'temporary',
            'order': 'temporary',
            'status': '3'
        }
        self.client.post(f"/requests/edit={request.id}/", data)  # type:ignore
        result = Request.objects.get(pk=request.id)  # type:ignore
        self.assertNotEqual(request.status, result.status)


class ModelTest(TestCase):
    def setUp(self):
        pass

    def create_new_customer(self):
        self.client.login(username='temporary', password='temporary')
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
        return result

    def test_model_status(self):
        customer = self.create_new_customer()
        model = Request(
            customer=customer,
            title='temporary',
            order='temporary',
            status='Em aberto',
        )
        model.save()
        response = Request.objects.get(title='temporary')  # type:ignore
        self.assertEqual(response.title, model.title)

