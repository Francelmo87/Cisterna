from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from .models import Titular, Dependente, Endereco

from .form import UsuarioForm


@login_required
def titular_list(request):
    template_name = 'titular/titular_list.html'
    titular = Titular.objects.filter()
    # CAMPO DE BUSCA
    search = request.GET.get('search')
    if search:
        titular = titular.filter(nome__icontains=search)
    # Paginação
    paginator = Paginator(titular, 10)
    page_number = request.GET.get('page')
    titular = paginator.get_page(page_number)
    context = {
        'titular_list': titular
    }
    return render(request, template_name, context)


@login_required
def titular_detail(request, pk):
    template_name = 'titular/titular_detail.html'
    obj = Titular.objects.get(pk=pk)
    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def titular_add(request):
    template_name = 'titular/titular_add.html'
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usuario:titular_list'))
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def titular_edit(request, pk):
    template_name = 'titular/titular_edit.html'
    obj = Titular.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usuarios:titular_list'))
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def titular_delete(request, pk):
    obj = Titular.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('usuarios:titular_list'))


@login_required
def dependente_list(request, pk):
    template_name = 'dependente/dependente_list.html'
    membro = Dependente.objects.filter(titular__pk=pk)
    context = {'dependente_list': membro}
    return render(request, template_name, context)


@login_required
def endereco_titular(request, pk):
    template_name = 'endereco/endereco_titular.html'
    endereco = Endereco.objects.filter(titular__pk=pk)
    context = {'endereco_list': endereco}
    return render(request, template_name, context)


#
# def produto_json(request, pk):
#     # Retorna o produto, id e estoque.
#     produto = Produto.objects.filter(pk=pk)
#     data = [item.to_dict_json() for item in produto]
#     return JsonResponse({'data': data})


# @login_required(login_url='/login/')
# def list_all_pets(request):
#     pet = Pet.objects.filter(active=True)
#     return render(request, 'list.html', {'pet':pet})
#
# @login_required(login_url='/login/')
# def list_user_pets(request):
#     pet = Pet.objects.filter(active=True, user=request.user)
#     return render(request, 'list.html', {'pet':pet})

#
# def titular_detail(request, pk):
#     global dias_consumo, dt_pedido
#     template_name = 'titular/titular_detail.html'
#     obj = Titular.objects.get(pk=pk)
#     cisterna = Cisterna.objects.get(titular__pk=pk)
#
#     membro = Membro.objects.filter(titular__pk=pk)
#
#     qtd_pessoas = Membro.objects.filter(titular__pk=pk, nome__isnull=False).count() + 1
#     volume = Cisterna.objects.filter(titular__pk=pk).annotate(volume_total=Sum('volume'))
#     for vol in volume:
#         dias_consumo = vol.volume_total // (qtd_pessoas * CONSUMO_PESSOA)
#
#     lista = Titular.objects.filter(pk=pk)
#     for i in lista:
#         if i.dt_validade < date.today():
#             situacao = Titular(pk=pk, active=False)
#             situacao.save(update_fields=["active"])
#
#         else:
#             situacao = Titular(pk=pk, active=True)
#             situacao.save(update_fields=["active"])
#
#     for dt in lista:
#         dt_pedido = dt.dt_pedido
#     tempo_uso = timedelta(dias_consumo)
#     if dt_pedido is not None:
#         dt_retorno = dt_pedido + tempo_uso
#     else:
#         dt_retorno = dt_pedido
#
#     context = {
#         'object': obj,
#         'cisterna': cisterna,
#         'dt_retorno': dt_retorno,
#         'membro_list': membro,
#     }
#     return render(request, template_name, context)
