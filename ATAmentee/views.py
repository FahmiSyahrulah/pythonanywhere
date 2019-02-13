from django.shortcuts import render
from .models import Mentee

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'mentee.html', {'mentees' : mentee})
# Create your views here.
