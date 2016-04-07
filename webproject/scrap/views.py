#-*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse

#from . import

def scrap(request):
    get_scrap = request.GET.get('scrap')
    if get_scrap == '11st':
        pass
    return render(request, 'scrap/scrap.html', {'status' : get_scrap})
