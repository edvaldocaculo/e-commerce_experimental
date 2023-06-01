# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Pagar(View):

    def get(*args, **kwargs):
        return HttpResponse('Pagar')


class FecharPedido(View):

    def get(*args, **kwargs):
        return HttpResponse('fechar pedido')


class Detalhe(View):

    def get(*args, **kwargs):
        return HttpResponse('detalhe do pedido')
