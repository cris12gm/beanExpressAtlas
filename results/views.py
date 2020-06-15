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
from results.barplot import barplotGene
from .models import pha1037

class results(TemplateView):
    template = 'results.html'

    def get(self, request):  

        return render(request, self.template, {
        })


    def post(self, request):  

        geneID = request.POST['geneID']
  #      samples = request.POST['samples']
 #       samplesHidden = request.POST['samples_hidden']
#        print (samples,samplesHidden)
        expression = pha1037.getGeneExpression(geneID)
        barPlot = ""
        samples = ""
        barPlot = barplotGene(expression,samples) 

        return render(request, self.template, {
            'geneID':geneID,
            'samples':samples,
            'barPlot':barPlot,
        })
 