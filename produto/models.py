import os

from django.conf import settings
from django.db import models
from PIL import Image


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField(max_length=255)
    imagem = models.ImageField(upload_to='imagem_salva/%Y/%m/%d', blank=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )

    def recize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size
        if original_width <= new_width:
            img_pill.close()
            return

        new_height = round((new_width * original_height)/original_width)
        new_img = img_pill.size((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 800
        if self.imagem:
            self.recize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'variação'
        verbose_name_plural = 'Variações'

    def __str__(self):
        return self.nome or self.produto.nome
