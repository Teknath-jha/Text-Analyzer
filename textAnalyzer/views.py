# I have created this file  -  Teknath jha 

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')
    # return HttpResponse('''<h1>Teknath jha</h1> <a href = "https://www.youtube.com"> Django Code </a>''')

def about(request):
    return HttpResponse("About Teknath jha   <a href='/capFirst'>go to Cap first</a> ")   

def analyze(request):
   
    # To get text from form 
    djText=request.POST.get('text','default')
    removePunc=request.POST.get('removePunc','off')
    upperCase=request.POST.get('upperCase','off')
    removeNewLine=request.POST.get('removeNewLine','off')
    charCount=request.POST.get('charCount','off')
    removeSpaces=request.POST.get('removeSpaces','off')
    
    puncations='''-_~`}{[]''"";:*/+=\|?/><,.!@#$%^&*()'''

    # Analyze text
    if removePunc == "on":
        
        analyzed=""
        for char in djText:
            if char not in puncations:
                analyzed=analyzed+char
        
        params={'purpose':'Remove Puncations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(upperCase == "on"):
        analyzed=""
        for char in djText:
            analyzed=analyzed+char.upper()
            
        params={'purpose':'Uppercase ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(removeNewLine == "on"):
        analyzed=""
        for char in djText:
            if char != '\n' and char !='\r':
                analyzed=analyzed+char
            
        params={'purpose':'Remove new line ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(charCount == "on"):
        analyzed=len(djText)
        analyzed='Length of string  :  '+str(analyzed)
        params={'purpose':'Length os given text  ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(removeSpaces == "on"):
        analyzed=""
        for index,char in enumerate(djText):
            if not(djText[index] == " " and djText[index] == " "):
                analyzed=analyzed+djText[index]
        params={'purpose':'Remove extra spaces  ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse(" Error  <br> <a href='/'>  Back </a>") 

    



# exercise to show naigation bar 
def capFirst(request):
    s='''
    <h2>Navigation Bar</h2><br>
    <a href="https://www.youtube.com">youtube</a> <br>
    <a href="https://www.amazon.com">Amazon</a> <br>
    <a href="https://www.zebronics.com">Zebronics</a> <br>
    <a href="https://www.google.com">Google</a> <br>
    '''
    return HttpResponse(s)

