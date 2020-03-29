"""
Author - Sahil Pabale
Project Title - Text Utils
Start date - 27/03/2020 Friday
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')  # return is compulsory, 1st argument = request, 2nd argument = file name
    # return HttpResponse('Your String Here')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    params = {}

    # Get the requirements
    text = request.POST.get('text', 'none')  # request.GET.get('name_value', 'default') will take the parameters
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('toupper', 'off')
    remnewline = request.POST.get('remnewline', 'off')
    remexspace = request.POST.get('remexspace', 'off')

    analyzed_text = ''

    # Punctuations
    puncs = '''!()-[]{}:;'"\,<>./@#$%^&*`~'''

    # Analyze the Text - Logic
    if removepunc == 'on':
        for char in text:
            if char not in puncs:
                analyzed_text += char
        params = {'analyzed_text': analyzed_text}
        text = analyzed_text

    if upper == 'on':
        analyzed_text = ''
        analyzed_text = text.upper()
        params = {'analyzed_text': analyzed_text}
        text = analyzed_text
    if remnewline == 'on':
        analyzed_text = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_text += char
        params = {'analyzed_text': analyzed_text}
        text = analyzed_text
    if remexspace == 'on':
        analyzed_text = ''
        for i, char in enumerate(text):
            if not (text[i - 1] == " " and text[i] == " "):
                analyzed_text += char

        params = {'analyzed_text': analyzed_text}

    # for sending data to html file we always use dictionary
    return render(request, 'analyze.html', params)
