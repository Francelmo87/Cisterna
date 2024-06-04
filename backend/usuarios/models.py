from django.db import models
from django.contrib.auth.models import User
from backend.base.models import TimeStampedModel


class Titular(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    dt_validade = models.DateField('Data da validade', null=True, blank=True)
    dt_pedido = models.DateField('Data do Pedido', null=True, blank=True)
    dt_entrega = models.DateField('Data da Entrega', null=True, blank=True)
    nome = models.CharField('Nome', max_length=70, blank=True)
    rg = models.PositiveIntegerField('RG', null=True, blank=True)
    cpf = models.PositiveIntegerField('CPF', null=True, blank=True)
    nis = models.PositiveIntegerField('NIS', null=True, blank=True)
    telefone = models.PositiveIntegerField('Telefone', null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Titulares'
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Membro(models.Model):
    titular = models.ForeignKey(Titular, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField('Nome', max_length=70, blank=True)
    cpf = models.PositiveIntegerField('CPF', null=True, blank=True)
    parentesco = models.CharField('Parentesco', max_length=20, blank=True)
    idade = models.PositiveIntegerField('Idade', null=True, blank=True)
    ocupacao = models.CharField('Ocupação', max_length=70, blank=True)
    renda = models.PositiveIntegerField('Renda', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Membros'
        ordering = ('nome',)


class Endereco(models.Model):
    titular = models.ForeignKey(Titular, on_delete=models.SET_NULL, null=True, blank=True)
    distrito = models.CharField('Distrito', max_length=20, blank=True)
    localidade = models.CharField('Localidade', max_length=20, blank=True)
    geolocalizacao = models.IntegerField('Geolocalização', blank=True)

    class Meta:
        verbose_name_plural = 'Endereços'
        ordering = ('distrito',)

    def __str__(self):
        return self.distrito


class Cisterna(models.Model):
    titular = models.ForeignKey(Titular, on_delete=models.SET_NULL, null=True, blank=True)
    codigo = models.CharField('código', max_length=6, unique=True)
    volume = models.CharField('Volume', max_length=6)

    class Meta:
        verbose_name_plural = 'Cisterna'

    def __str__(self):
        return self.volume
