from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Request
from .forms import RequestForm
from customers.models import Customer


@login_required()
@csrf_exempt
def get_table(request):
    query = Request.objects.all()  # type:ignore
    data = {'requests': query}
    return render(request, 'requests_table.html', data)


@login_required()
@csrf_exempt
def get_form(request):
    form = RequestForm()
    data = {'form': form}
    return render(request, "new_request.html", data)


@login_required()
@csrf_exempt
def create_request(request):
    form = RequestForm(request.POST)
    x = True
    # Form choice is return invalid, need correction
    if x:
        try:
            customer_id = request.POST['choice']
            customer = Customer.objects.get(pk=customer_id)  # type: ignore
            status = get_status(request.POST['status'])
        except KeyError:
            return HttpResponse('Formulario incorreto', status=500)

        new_request = Request(
            customer=customer,
            title=request.POST['title'],
            order=request.POST['order'],
            status=status
        )
        new_request.save()
        return HttpResponse('Chamado criado!', status=200)
    else:
        return HttpResponse('Formulario incorreto', status=500)


@login_required()
@csrf_exempt
def delete_request(request, id):
    try:
        query = Request.objects.get(pk=id)  # type:ignore
    except Request.DoesNotExist:  # type:ignore
        return HttpResponse("Chamado não encontrado", status=500)
    if query:
        query.delete()
        return HttpResponse("Chamado deletado", status=200)
    return HttpResponse("Chamado não encontrado", status=500)


@login_required()
@csrf_exempt
def edit_request(request, id):
    query = Request.objects.get(pk=id)  # type: ignore
    if request.method == 'POST':
        post = request.POST
        try:
            status = post['status']
            customer_id = request.POST['choice']
            query.title = post['title']
            query.order = post['order']
            query.status = get_status(status)
            query.customer = Customer.objects.get(pk=customer_id)  # type: ignore
            query.save()
            return HttpResponse('Chamado editado!', status=200)
        except KeyError:
            return HttpResponse('Formulario incorreto!', status=500)
    else:
        form = RequestForm(instance=query)
        data = {'form_request': form, 'id': query.id}
        return render(request, "edit_request.html", data)


def get_status(value):
    options = ['Em aberto', 'Concluido', 'Em aguardo', 'Em aberto']
    return options[int(value)]
