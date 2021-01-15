from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyze(request):
    txt = request.GET.get('text', 'default')
    is_punc = request.GET.get('remPunc', 'off')

    if is_punc == 'on':
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for i in txt:
            if i in punc:
                txt = txt.replace(i, "")
        analyzed = txt

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Remove punctuations not ticked')
