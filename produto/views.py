from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import ListView, View


class ListaProduto(ListView):

    def get(*args, **kwargs):
        return HttpResponse('produto')


class DetalhesProduto(View):
    def get(*args, **kwargs):
        return HttpResponse('detalhe produto')


class AdicionarAoCarrinho(View):
    def get(*args, **kwargs):
        return HttpResponse('adicionar produto')


class RemoverDoCarrinho(View):
    def get(*args, **kwargs):
        return HttpResponse('remver')


class Carrinho(View):
    def get(*args, **kwargs):
        return HttpResponse('carrinho')


class Finalizar(View):
    def get(*args, **kwargs):
        return HttpResponse('finalizar')
