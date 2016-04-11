#-*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse

import sys
import os

current_path = os.path.abspath('')
sys.path.append(current_path + '/study/kma/django/webproject/module')

import db_module

def scrap(request):
    get_scrap = request.GET.get('scrap')
    if get_scrap == '11st':
        pass
    return render(request, 'scrap/scrap.html', {'status' : get_scrap})
