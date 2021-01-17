from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyze(request):
    txt = request.POST.get('text', 'default')
    is_punc = request.POST.get('remPunc', 'off')
    is_fullCaps = request.POST.get('fullCaps', 'off')
    is_extraspace = request.POST.get('remSpace', 'off')
    is_remLine = request.POST.get('remLine', 'off')

    if is_punc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in txt:
            if i not in punc:
                analyzed = analyzed + i

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        txt = analyzed

    if is_fullCaps == 'on':
        analyzed = ""
        for i in txt:
            analyzed = analyzed + i.upper()

        params = {'purpose': 'Capitalized letters', 'analyzed_text': analyzed}
        txt = analyzed

    if is_extraspace == "on":
        analyzed = ""
        for index, char in enumerate(txt):
            if not(txt[index] == " " and txt[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra spaces', 'analyzed_text': analyzed}
        txt = analyzed

    if is_remLine == 'on':
        analyzed = ""
        for i in txt:
            if i != '\n' and i != "\r":
                analyzed = analyzed + i

        params = {'purpose': 'Removed blank lines', 'analyzed_text': analyzed}

    if(is_punc != "on" and is_fullCaps != "on" and is_extraspace != "on" and is_remLine != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
