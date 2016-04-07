import os, subprocess, commands, re
#-*- coding: utf-8 -*-

def nlp_input(get_query):
    input_dir = '/home/yjm/study/kma/input_txt'
    if get_query is not None:
        with open(input_dir, 'wb') as f:
            f.write(get_query.encode('utf-8'))

def nlp_output(output_type='mecab'):
    input_dir = '/home/yjm/study/kma/input_txt'
    output_dir = '/home/yjm/study/kma/output_txt'
    if output_type == 'mecab':
        command = 'mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic < {input} > {output}'.format(input=input_dir, output=output_dir)
    else:
        command = '/home/yjm/NLP/kma_batch /home/yjm/NLP/dict 4 < {input} > {output}'.format(input=input_dir, output=output_dir)

    call_result = subprocess.call(command, shell=True)
    print str(call_result)

    line = ''
    result = '<div><pre>'
    with open(output_dir, 'rb') as f:
        while True:
            line = f.readline()
            result += line
            if not line: break
    result += '</pre></div>'
    return result

def nlp_batch():
    command_mecab = 'time mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic < /home/yjm/NLP/test10.txt > result.txt'
    status_macab, call_result_mecab = commands.getstatusoutput(command_mecab)# subprocess.call(command, shell=True)

    command_kma = 'time /home/yjm/NLP/kma_batch /home/yjm/NLP/dict 4 < /home/yjm/NLP/test10.txt > result.txt'
    status_kma, call_result_kma = commands.getstatusoutput(command_kma)# subprocess.call(command, shell=True)

    call_result_mecab = re.sub('\n', '<br>', call_result_mecab)
    call_result_kma = re.sub('\n', '<br>', call_result_kma)

    return call_result_mecab, call_result_kma
