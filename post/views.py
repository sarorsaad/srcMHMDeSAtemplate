from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse, reverse_lazy
from .forms import CRUDForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class PostList(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/list.html'

class PostDetail(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'postS'
    template_name = 'post/detail.html'

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    form_class = CRUDForm
    template_name = 'post/create.html'
    success_url = reverse_lazy('post_list')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = CRUDForm
    template_name = 'post/update.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post_list')
