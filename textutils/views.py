# I have created this file - Abhishek

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Abhishek', 'place': 'Mars'}

    #return HttpResponse("<h1>Home</h1>")
    return render(request, 'index.html', params)

def analyze(request):

    # GET the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    

    print(djtext)
    print(removepunc)
    # analyzed = djtext

    # Check which checkbox value is on
    if removepunc == 'on':

        punctuations = '''.,?!:;'"()[]{}...-—–/&*^%$#@`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    
    if(capitalize == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPER CASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    
    if(charcount == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
            print(char)
            count = count + 1    
        params = {'purpose': 'Character Count', 'analyzed_text': count}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if(removepunc != 'on' and capitalize != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error: Please Enable anyone toggle")
    

    return render(request, 'analyze.html', params)
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")


# def charcount(request):
#     return HttpResponse("charcount")
