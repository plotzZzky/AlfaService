from django import forms
from django.db.utils import ProgrammingError

from .models import Request
from customers.models import Customer


options = [
    (0, 'Seleciona uma opção'),
]


def get_customers():
    try:
        query = Customer.objects.all()  # type:ignore
        if query >= 1:
            for item in query:
                item = (item.id, item.cpf)
                options.append(item)
            return options
        else:
            pass
    except TypeError:
        return options
    except ProgrammingError:
        return options


Choices = get_customers()
Status = [
    (0, 'Selecione uma opção'),
    (1, 'Concluido'),
    (2, 'Em aguardo'),
    (3, 'Em aberto')
]


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["customer", "title", "order"]

    customer = forms.ChoiceField(label="", choices=Choices,
                                 widget=forms.Select(attrs={'id': 'Choice', 'class': 'select'}))
    status = forms.ChoiceField(label="", choices=Status, widget=forms.Select(attrs={'id': 'Status', 'class': 'select'}))
    title = forms.CharField(label="", min_length=10, widget=forms.TextInput(
        attrs={'placeholder': 'Titulo do pedido', 'id': 'Title', 'class': 'inputForm'}))
    order = forms.CharField(label="", min_length=20, widget=forms.Textarea(
        attrs={'placeholder': 'Pedido do cliente', 'id': 'Order'}))
