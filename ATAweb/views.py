from django.shortcuts import render

def web(request):
    return render(request, 'home.html')
# Create your views here.
