import itertools
from django.conf import settings
import datetime
import os
from enum import Enum
from functools import reduce
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import FormView, DetailView, TemplateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from sqlalchemy import inspect

class results(TemplateView):
    template = 'results.html'

    def get(self, request):  

        return render(request, self.template, {
        })
    def post(self, request):  

        return render(request, self.template, {
        })
 