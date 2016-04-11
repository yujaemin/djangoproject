#-*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from . import nlpModule

def nlp(request):
    """ get_query : 웹에서 입력칸에 입력받은 문자열
        get_batch : batch test 버튼을 입력했을때 넘어오는 값

        result_mecab : get_query 문장을 mecab으로 NLP 분석했을 때 결과값
        result_kma : get_query 문장을 kma로 NLP 분석했을 때 결과값
        result_mecab_batch = 약30mb 텍스트 파일을 mecab으로 NLP 분석했을 때 걸린 시간
        result_kma_batch = 약30mb 텍스트 파일을 kma로 NLP 분석했을 때 걸린 시간
        result_file_mecab = 업로드한 파일을 mecab으로 NLP 분석했을 때 결과값
        result_file_kma = 업로드한 파일을 kma로 NLP 분석했을 때 결과값
        result_file_mecab_time = 업로드한 파일을 mecab으로 NLP 분석했을 때 걸린 시간
        result_file_kma_time = 업로드한 파일을  kma로 NLP 분석했을 때 걸린 시간
    """
    get_query = request.GET.get('query')
    get_batch = request.GET.get('batch')
    result_mecab = ''
    result_kma = ''
    result_mecab_batch = ''
    result_kma_batch = ''
    result_file_mecab = ''
    result_file_kma = ''
    result_file_mecab_time = ''
    result_file_kma_time = ''

    if get_query is not None:
        nlpModule.nlp_input(get_query)
        result_mecab = nlpModule.nlp_output('mecab')
        result_kma = nlpModule.nlp_output('kma')

    if get_batch is not None:
        result_mecab_batch, result_kma_batch = nlpModule.nlp_batch()

    if request.method == 'POST':
        status, result = nlpModule.file_upload(request)
        if status is True:
            nlpModule.nlp_input(result)
            result_file_mecab, result_file_kma, result_file_mecab_time, result_file_kma_time = nlpModule.nlp_result_elapse_time()
        else:
            result_file_mecab_time = result
            result_file_kma_time = result

    return render(request, 'nlp/nlp.html', {
        'result_MECAB' : result_mecab,
        'result_KMA' : result_kma,
        'result_MECAB_batch' : result_mecab_batch,
        'result_KMA_batch' : result_kma_batch,
        'result_file_MECAB' : result_file_mecab,
        'result_file_KMA' : result_file_kma,
        'result_file_MECAB_time' : result_file_mecab_time,
        'result_file_KMA_time' : result_file_kma_time,
        })
