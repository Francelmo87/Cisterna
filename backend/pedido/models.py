from django.db import models

from backend.usuarios.models import Titular
from backend.base.models import TimeStampedModel

STATUS_CHOICES = (
    ('S', 'Solicitado'),
    ('A', 'Atendido'),
    ('P', 'Pendente'),
    ('C', 'Cancelado'),
)


# Create your models here.
class Pedido(TimeStampedModel):
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)
    titular = models.ForeignKey(
        Titular,
        on_delete=models.SET_NULL,
        related_name='titulares',
        null=True, blank=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pk} - {self.created.strftime("%d-%m-%Y)")} - {self.status}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=20, decimal_places=2)
