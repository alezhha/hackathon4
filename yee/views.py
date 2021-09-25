from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Letter

# Create your views here.

def main(request):
    return render(request, "index.html")

def send(request):
    if request.method == 'POST':
        letter = Letter()
        letter.text = request.POST.get('text')
        letter.email = request.POST.get('email')
        letter.address = request.POST.get('address')
        letter.messages = request.POST.get('messages')
        letter.save()
    return HttpResponseRedirect('/')