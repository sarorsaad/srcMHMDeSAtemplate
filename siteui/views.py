from django.shortcuts import render

from post.models import Post

def index(request):
    context = {
        'posts': Post.objects.all(),
        'last_three_posts': Post.objects.all().order_by('-id')[:3],
        'last_four_posts': Post.objects.all().order_by('-id')[:4],
    }
    return render(request, 'siteui/index.html', context=context)


def about(request):
    return render(request, 'siteui/about.html')

def contact(request):
    return render(request, 'siteui/contact.html')

def show(request, pk):
    context = {}
    context['post'] = Post.objects.get(pk=pk)
    return render(request, 'siteui/show.html', context=context)

