# Generated by Django 5.0 on 2024-01-30 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='modificado em')),
                ('dt_validade', models.DateField(blank=True, null=True, verbose_name='Data da validade')),
                ('dt_pedido', models.DateField(blank=True, null=True, verbose_name='Data do Pedido')),
                ('dt_entrega', models.DateField(blank=True, null=True, verbose_name='Data da Entrega')),
                ('nome', models.CharField(blank=True, max_length=70, verbose_name='Nome')),
                ('rg', models.PositiveIntegerField(blank=True, null=True, verbose_name='RG')),
                ('cpf', models.PositiveIntegerField(blank=True, null=True, verbose_name='CPF')),
                ('nis', models.PositiveIntegerField(blank=True, null=True, verbose_name='NIS')),
                ('telefone', models.PositiveIntegerField(blank=True, null=True, verbose_name='Telefone')),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Titulares',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=70, verbose_name='Nome')),
                ('cpf', models.PositiveIntegerField(blank=True, null=True, verbose_name='CPF')),
                ('parentesco', models.CharField(blank=True, max_length=20, verbose_name='Parentesco')),
                ('idade', models.PositiveIntegerField(blank=True, null=True, verbose_name='Idade')),
                ('ocupacao', models.CharField(blank=True, max_length=70, verbose_name='Ocupação')),
                ('renda', models.PositiveIntegerField(blank=True, null=True, verbose_name='Renda')),
                ('titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.titular')),
            ],
            options={
                'verbose_name_plural': 'Membros',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrito', models.CharField(blank=True, max_length=20, verbose_name='Distrito')),
                ('localidade', models.CharField(blank=True, max_length=20, verbose_name='Localidade')),
                ('geolocalizacao', models.IntegerField(blank=True, verbose_name='Geolocalização')),
                ('titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.titular')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
                'ordering': ('distrito',),
            },
        ),
        migrations.CreateModel(
            name='Cisterna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, unique=True, verbose_name='código')),
                ('volume', models.CharField(max_length=6, verbose_name='Volume')),
                ('titular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.titular')),
            ],
            options={
                'verbose_name_plural': 'Cisterna',
            },
        ),
    ]
