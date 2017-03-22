from django.shortcuts import render


def index(request):
    return render(request, 'consulting/index.html')


def status(request):
    return render(request, 'consulting/status.html')
