from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Patient

# Define a class-based view for home page
class HomePage(TemplateView):
    template_name = 'hospital/home.html'

# Define a class-based view for thank you page
class ThankYouPage(TemplateView):
    template_name = 'hospital/thankyou.html'

# Define a class-based view for creating a new patient record
class PatientCreateView(CreateView):
    model = Patient
    # Use all fields of the Patient model in the form
    fields = "__all__"
    # Set the URL to redirect to on successful form submission
    success_url = reverse_lazy('hospital:thankyou')
    
class PatientListView(ListView):
    model = Patient
    template_name = 'hospital/patient_list.html'
    context_object_name = 'patient_list'
    
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'hospital/patient_detail.html'
    context_object_name = 'patient'
class PatientUpdateView(UpdateView):
    model = Patient
    fields = "__all__"  # Specify the fields to be updated
    template_name = 'hospital/patient_update.html'  # Template for the update form
    success_url = reverse_lazy('hospital:patient_list')
    
class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('hospital:patient_list')  # Specify the URL to redirect to after deletion
    template_name = 'hospital/patient_delete.html' 