from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'MS DHONI',
       'age':37}
    return render(request,'csk.html',context=d)