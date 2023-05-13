from django.shortcuts import render

def index(request):
    return render(request, 'siteui/index.html')

def about(request):
    return render(request, 'siteui/about.html')

def contact(request):
    return render(request, 'siteui/contact.html')

def show(request,pk):
    return render(request, 'siteui/show.html')
