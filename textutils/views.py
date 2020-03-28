"""
Author - Sahil Pabale
Project Title - Text Utils
Start date - 27/03/2020 Friday
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')  # return is compulsory, 1st argument = request, 2nd argument = file name
    # return HttpResponse('<h1>Home Page</h1><br>')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    # Get the Text
    text = request.GET.get('text', 'none')  # request.GET.get('name_value', 'default') will take the parameters
    removepunc = request.GET.get('removepunc', 'off')
    upper = request.GET.get('toupper', 'off')

    analyzed_text = ''

    # Punctuations
    puncs = '''!()-[]{}:;'"\,<>./@#$%^&*`~'''

    # Analyze the Text - Logic

    if removepunc == 'on':
        for char in text:
            if char not in puncs:
                analyzed_text += char
    elif upper == 'on':
        analyzed_text = ''
        analyzed_text = text.upper()


    # for sending data to html file we always use dictionary
    params = {'text': text, 'analyzed_text': analyzed_text, 'puncstate':removepunc}

    return render(request, 'analyze.html', params)
