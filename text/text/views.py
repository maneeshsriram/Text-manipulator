from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyze(request):
    txt = request.GET.get('text', 'default')
    is_punc = request.GET.get('remPunc', 'off')
    is_fullCaps = request.GET.get('fullCaps', 'off')
    is_extraspace = request.GET.get('remSpace', 'off')
    is_remLine = request.GET.get('remLine', 'off')

    if is_punc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in txt:
            if i not in punc:
                analyzed = analyzed + i

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif is_fullCaps == 'on':
        analyzed = ""
        for i in txt:
            analyzed = analyzed + i.upper()

        params = {'purpose': 'Capitalized letters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif is_extraspace == "on":
        analyzed = ""
        for index, char in enumerate(txt):
            if not(txt[index] == " " and txt[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif is_remLine == 'on':
        analyzed = ""
        for i in txt:
            if i != '\n' and i != "\r":
                analyzed = analyzed + i

        params = {'purpose': 'Removed blank lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('<h1>Please tick any checkbox</h1>')
