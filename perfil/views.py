# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Criar(View):
    def get(*args, **kwargs):
        return HttpResponse('Criar')


class Atualizar(View):
    def get(*args, **kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def get(*args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(*args, **kwargs):
        return HttpResponse('Logout')
