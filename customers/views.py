from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Customer
from .forms import CustomerForm


@login_required()
@csrf_exempt
def get_table(request):
    query = Customer.objects.all()  # type:ignore
    data = {'customers': query}
    return render(request, 'customers_table.html', data)


@login_required()
@csrf_exempt
def get_form(request):
    form = CustomerForm()
    data = {'form': form}
    return render(request, "new_customer.html", data)


@login_required()
@csrf_exempt
def create_customer(request):
    cpf = request.POST.get('cpf', None)
    try:
        x = Customer.objects.get(cpf=cpf)  # type:ignore
        return HttpResponse('Cpf ja existe')
    except Customer.DoesNotExist:  # type: ignore
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            customer = Customer(
                cpf=cpf,
                name=request.POST['name'],
                lastname=request.POST['lastname'],
                address=request.POST['address'],
                city=request.POST['city'],
                telephone=request.POST['telephone'],
                email=request.POST['email'],
            )
            customer.save()
            return HttpResponse('Cliente criado!', status=200)
        return HttpResponse('Formulario incorreto!', status=500)


@login_required()
@csrf_exempt
def delete_customer(request, id):
    try:
        query = Customer.objects.get(id=id)  # type:ignore
        if query:
            query.delete()
            return HttpResponse("Cliente deletado!", status=200)
        else:
            return HttpResponse("cliente não encontrado", status=404)
    except Customer.DoesNotExist:
        return HttpResponse("cliente não encontrado", status=404)


@login_required()
@csrf_exempt
def edit_customer(request, id):
    try:
        query = Customer.objects.get(pk=id)  # type: ignore
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                post = request.POST
                query.cpf = post['cpf']
                query.name = post['name']
                query.lastname = post['lastname']
                query.city = post['city']
                query.address = post['address']
                query.telephone = post['telephone']
                query.email = post['email']
                query.save()
                return HttpResponse('Cliente editado!', status=202)
            return HttpResponse('Formulario invalido!', status=500)
        else:
            form = CustomerForm(instance=query)
            data = {'form_customer': form, 'id': query.id}
            return render(request, "edit_customer.html", data)
    except KeyError:
        return HttpResponse("Id error", status=404)
