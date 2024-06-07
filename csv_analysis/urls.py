from django.urls import path
from csv_analysis import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('analysis/<str:file_name>/', views.data_analysis, name='data_analysis'),
]