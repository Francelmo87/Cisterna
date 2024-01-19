from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import date, timedelta

from .models import Titular, Membro, Endereco


@login_required
def membro_list(request, pk):
    template_name = 'membro_list.html'
    membro = Membro.objects.filter(titular__pk=pk)
    context = {'membro_list': membro}
    return render(request, template_name, context)


@login_required
def endereco_titular(request, pk):
    template_name = 'endereco_titular.html'
    endereco = Endereco.objects.filter(titular__pk=pk)
    context = {'endereco_list': endereco}
    return render(request, template_name, context)


@login_required
def titular_list(request):
    template_name = 'titular_list.html'
    titular = Titular.objects.all()
    search = request.GET.get('search')
    if search:
        titular = titular.filter(nome__icontains=search)
    now = date.today()
    # year = timedelta(days=365)
    # validade = titular.values("inicio").annonnate(sum(year))

    context = {
        'titular_list': titular,
        'now': now
        # 'tempo_ativo': validade
       }
    print(context)
    return render(request, template_name, context)


@login_required
def titular_detail(request, pk):
    template_name = 'titular_detail.html'
    obj = Titular.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def tempo_ativo(request):
    year = timedelta(days=365)
    validade = date.today() + year
    context = {'tempo_ativo': validade}
    return render(request, context)







#
#
# @login_required
# def produto_add(request):
#     form = ProdutoForm(request.POST or None)
#     template_name = 'produto_form.html'
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('produto:produto_list'))
#     context = {'form': form}
#     return render(request, template_name, context)
#
# #
# @login_required
# def produto_update(request, pk):
#     template_name = 'produto_update.html'
#     obj = Produto.objects.get(pk=pk)
#     form = ProdutoForm(request.POST or None, instance=obj)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('produto:produto_list'))
#     context = {'form': form}
#     return render(request, template_name, context)
#
#
# @login_required
# def produto_delete(request, pk):
#     obj = Produto.objects.get(pk=pk)
#     obj.delete()
#     return HttpResponseRedirect(reverse('produto:produto_list'))
#
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


# Paginação
    # paginator = Paginator(objects, 10)
    # page_number = request.GET.get('page')
    # objects = paginator.get_page(page_number)