from django.urls import path
from . import views


app_name='patient'
urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
]
