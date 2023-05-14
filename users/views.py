from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


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
