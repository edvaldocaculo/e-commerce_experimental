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


admin.site.register(models.Variacao)
