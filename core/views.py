from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from customers.models import Customer
from requests.models import Request


@login_required()
def home(request):
    return render(request, 'app.html')


def about(request):
    return render(request, 'about.html')


def create_info(request):
    maria = Customer(cpf="00011100011", name="Maria", lastname="Teixeira", city="Canoas", address="rua brasil, 118",
                     telephone="(51)90908080", email="mariat@mail.com")
    maria.save()
    jose = Customer(cpf="11100011100", name="Jose", lastname="daRosa", city="Esteio", address="rua do mar, 80",
                    telephone="(51)90909090", email="jose.rosa@mail.com")
    jose.save()
    paulo = Customer(cpf="12812812812", name="Paulo", lastname="Castro", city="Canoas", address="rua aleatoria, 12",
                     telephone="(51)11111111", email="")
    paulo.save()
    chamado1 = Request(customer=maria, title="instalação de internet",
                       order="Cliente solicita instalção de internte 100mb na parte da noite", status="Em aberto")
    chamado1.save()
    chamado2 = Request(customer=paulo, title="Modem com defeito",
                       order="Cliente informa que seu modem fica desligando sozinho", status="Em aguardo")
    chamado2.save()
    return redirect("/")
