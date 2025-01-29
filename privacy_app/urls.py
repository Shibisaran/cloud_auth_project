from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('request_access/<int:file_id>/', views.request_access, name='request_access'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
]
