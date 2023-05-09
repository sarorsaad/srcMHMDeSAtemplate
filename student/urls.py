from django.urls import path
from . import views

# Define the URL patterns for the app
app_name='student'

urlpatterns = [
    path('', views.allStudent, name='all'),  # Matches the root URL and calls the allStudent view function
    path('add/', views.addStudent, name='addstudent'),  # Matches the /add/ URL and calls the addStudent view function
    path('edit/', views.editStudent, name='editstudent'),  # Matches the /edit/ URL and calls the editStudent view function
]
