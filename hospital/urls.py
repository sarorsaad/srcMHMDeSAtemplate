from django.urls import path
from .views import HomePage, ThankYouPage, PatientCreateView, PatientListView, PatientDetailView,PatientUpdateView,PatientDeleteView

app_name = 'hospital'

urlpatterns = [
    path('home/', HomePage.as_view(), name='home'),
    path('thankyou/', ThankYouPage.as_view(), name='thankyou'),
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/list/', PatientListView.as_view(), name='patient_list'),
    path('patient_detail/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
