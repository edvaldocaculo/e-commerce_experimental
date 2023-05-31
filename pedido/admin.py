from django.contrib import admin

from . import models


class ItemPedidoInlines(admin.TabularInline):
    model = models.ItemPedido
    extra = 1


@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInlines
    ]


admin.site.register(models.ItemPedido)
