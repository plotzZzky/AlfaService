from django import forms

from .models import Request
from customers.models import Customer


def get_customers():
    query = Customer.objects.all()  # type:ignore
    options = [
        (0, 'Seleciona uma opção'),

    ]
    for item in query:
        item = (item.id, item.cpf)
        options.append(item)
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
    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Titulo do pedido', 'id': 'Title', 'class': 'inputForm'}))
    order = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Pedido do cliente', 'id': 'Order'}))
