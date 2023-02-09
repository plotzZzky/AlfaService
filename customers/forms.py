from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["cpf", "name", "lastname", "city", "address", "telephone", "email"]

    cpf = forms.CharField(max_length=255, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Cpf', 'id': 'Cpf', 'class': 'inputForm'}))
    name = forms.CharField(max_length=255, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'id': 'Name', 'class': 'inputForm'}))
    lastname = forms.CharField(max_length=255, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Sobrenome', 'id': 'Lastname', 'class': 'inputForm'}))
    address = forms.CharField(max_length=300, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Endereco', 'id': 'Address', 'class': 'inputForm'}))
    city = forms.CharField(max_length=255, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Cidade', 'id': 'City', 'class': 'inputForm'}))
    telephone = forms.CharField(max_length=255, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Telefone', 'id': 'Telephone', 'class': 'inputForm'}))
    email = forms.CharField(required=False,max_length=255, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'id': 'Email', 'class': 'inputForm'}))
