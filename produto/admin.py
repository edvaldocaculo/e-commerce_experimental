from django.contrib import admin

from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]
    list_display = [
        'nome', 'descricao_curta', 'get_preco_formatado',
        'get_preco_promo_formatado',
    ]


admin.site.register(models.Variacao)
