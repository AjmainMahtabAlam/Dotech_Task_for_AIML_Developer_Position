from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_signature, name='upload_signature'),
]
