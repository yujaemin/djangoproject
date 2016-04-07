#-*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from . import nlpModule

def nlp(request):
    get_query = request.GET.get('query')
    get_batch = request.GET.get('batch')
    result_mecab = ''
    result_kma = ''
    result_mecab_batch = ''
    result_kma_batch = ''
    if get_query is not None:
        nlpModule.nlp_input(get_query)

        result_mecab = nlpModule.nlp_output('mecab')
        result_kma = nlpModule.nlp_output('kma')
    if get_batch is not None:
        result_mecab_batch, result_kma_batch = nlpModule.nlp_batch()
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name
            UPLOAD_DIR = '/home/yjm/study/kma/'
            f = open('%s/%s' % (UPLOAD_DIR, filename), 'wb')
            for chunk in file.chunks():
                print chunk
                print type(chunk)
                f.write(chunk)
            f.close()
        print filename
    return render(request, 'nlp/nlp.html', {
        'result_MECAB' : result_mecab,
        'result_KMA' : result_kma,
        'result_MECAB_batch' : result_mecab_batch,
        'result_KMA_batch' : result_kma_batch})
