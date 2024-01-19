from django.contrib import admin

from .models import Titular, Endereco, Membro


class MembroInline(admin.TabularInline):
    model = Membro
    extra = 0
    # list_display = ('nome', 'cpf', 'parentesco', 'idade', 'ocupacao', 'renda', 'usuario',)


class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 0
    # list_display = ('distrito', 'localidade', 'geolocalizacao', 'usuario',)


@admin.register(Titular)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = (MembroInline, EnderecoInline)
    list_display = ('inicio', 'fim', 'nome', 'rg', 'cpf', 'nis', 'telefone', 'active',)





