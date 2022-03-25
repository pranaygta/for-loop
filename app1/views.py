from django.shortcuts import render

# Create your views here.
def vishnu(request):
    d={'name':'pranay'}
    return render(request,'vishnu.html',d)
