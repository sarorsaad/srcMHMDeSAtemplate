from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import RegistrationForm


from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'users/home.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        messages.info(self.request, 'Welcome to your profile.')
        return reverse_lazy('profile')

    def form_invalid(self, form):
        messages.error(self.request, 'Error: Invalid username or password.')
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    form_class = RegistrationForm
    redirect_authenticated_user = True
    template_name = 'registration/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')
    
    def dispatch(self, request, *args, **kwargs):
      if request.user.is_authenticated:
        return redirect('profile')
      return super(RegisterView, self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)