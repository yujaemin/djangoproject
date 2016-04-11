import os, subprocess, commands, re
#-*- coding: utf-8 -*-

""" 기본 변수 세팅
"""
input_dir = '/home/yjm/study/kma/input_txt'
output_dir = '/home/yjm/study/kma/output_txt'
command_kma = 'time /home/yjm/NLP/kma_batch /home/yjm/NLP/dict 4 < /home/yjm/NLP/test10.txt > result.txt'
command_mecab = 'time mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic < /home/yjm/NLP/test10.txt > result.txt'
command_kma_f = 'time /home/yjm/NLP/kma_batch /home/yjm/NLP/dict 4 < {input} > {output}'.format(input=input_dir, output=output_dir)
command_mecab_f = 'time mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic < {input} > {output}'.format(input=input_dir, output=output_dir)

def print_result(output_dir):
    """ parameter : 아웃풋 파일의 경로
        return : 파일 내용 문자열
    """
    line = ''
    result = '<div><pre>'
    with open(output_dir, 'rb') as f:
        while True:
            line = f.readline()
            result += line
            if not line: break
    result += '</pre></div>'
    return result

def print_total_time(call_result):
    """ parameter : NLP 배치파일을 수행한 시간 결과값
        return : 불필요한 값을 제거하고 HTML 형식에 맞게 변환한 문자열
    """
    result = '<div><pre>total time'
    call_result = re.findall('\d+.*elapsed?', call_result)[0]
    call_result = re.split('\s', call_result)
    for cr in call_result:
        result += '</br>' + cr
    result += '</pre></div>'
    return result

def nlp_input(get_query):
    """ parameter : NLP 배치파일을 수행할 문자열
        받은 parameter를 파일에 씀(encoding = utf-8)
        return : 없음
    """
    if get_query is not None:
        with open(input_dir, 'wb') as f:
            f.write(get_query.encode('utf-8'))

def nlp_output(output_type='mecab'):
    """ parameter : mecab이나 kma
        return : 받은 parameter에 해당하는 NLP 배치파일 수행한 결과값
    """
    if output_type == 'mecab':
        command = command_mecab_f
    else:
        command = command_kma_f
    call_result = subprocess.call(command, shell=True)

    result = print_result(output_dir)
    return result

def nlp_batch():
    """ parameter : 없음
        return : NLP 배치파일 수행한 시간 결과값
    """
    status_kma, call_result_kma = commands.getstatusoutput(command_kma)
    kma_time = print_total_time(call_result_kma)

    status_macab, call_result_mecab = commands.getstatusoutput(command_mecab)
    mecab_time = print_total_time(call_result_mecab)
    return mecab_time, kma_time

def file_upload(request):
    """ parameter : 웹에서 POST로 받은 요청값
        받은 요청중에 파일이 있는지 확인함
        return : 파일 내부에 있는 문자열
        파일을 서버에 저장은 하지 않음
    """
    try:
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name
            UPLOAD_DIR = '/home/yjm/study/kma/'
            query = ''
            with open('%s/%s' % (UPLOAD_DIR, filename), 'w') as f:
                for chunk in file.chunks():
                    chunk = unicode(chunk, 'euc-kr')
                    query += chunk
                return True, query
    except Exception, e:
        return False, e

def nlp_result_elapse_time():
    """ parameter : 없음
        return : 업로드한 파일을 수행한 결과와 시간
    """
    status_kma, call_result_kma = commands.getstatusoutput(command_kma_f)
    kma_time = print_total_time(call_result_kma)
    kma = print_result(output_dir)

    status_macab, call_result_mecab = commands.getstatusoutput(command_mecab_f)
    mecab_time = print_total_time(call_result_mecab)
    mecab = print_result(output_dir)

    return mecab, kma, mecab_time, kma_time
