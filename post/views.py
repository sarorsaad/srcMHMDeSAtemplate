from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse, reverse_lazy
from .forms import CRUDForm

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/list.html'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'postS'
    template_name = 'post/detail.html'

class PostCreate(CreateView):
    model = Post
    form_class = CRUDForm
    template_name = 'post/create.html'
    success_url = reverse_lazy('post_list')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    form_class = CRUDForm
    template_name = 'post/update.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post_list')
