from django.contrib import admin

from .models import Titular, Endereco, Membro, Cisterna


class MembroInline(admin.TabularInline):
    model = Membro
    extra = 0


class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 0


class CisternaInline(admin.TabularInline):
    model = Cisterna
    extra = 0


@admin.register(Titular)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = (MembroInline, EnderecoInline, CisternaInline)
    list_display = ('nome', 'rg', 'cpf', 'nis', 'telefone', 'active',)

