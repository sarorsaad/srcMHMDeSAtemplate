from django.urls import path
from . import views


app_name = 'staff'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('create/', views.Create.as_view(), name='create'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
]
