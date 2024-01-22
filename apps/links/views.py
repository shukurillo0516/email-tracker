from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse


class LinkView(View):
    def get(self, request, name=None, *args, **kwargs):
        return JsonResponse({1: 1})
