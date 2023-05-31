from django.contrib.auth.models import User
from django.db import models


class Pedido(models.Model):
    user = models.ForeignKey(
        User, verbose_name="usuário", on_delete=models.CASCADE
        )
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido n. {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(verbose_name='variação', max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField(verbose_name='preço')
    preco_promocional = models.FloatField(default=0.0, verbose_name='promoção')
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.pedido}'
