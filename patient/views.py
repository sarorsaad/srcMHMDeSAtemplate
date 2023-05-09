from django.shortcuts import render
from .models import Patient

def patient_list(request):
    # Get all patient objects from the database
    patients = Patient.objects.all()
    # Render the template with the patients queryset as the context
    return render(request, 'patient/patient.html', {'patients': patients})
