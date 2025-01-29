from django import forms
from .models import File, AccessRequest

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['filename', 'file_hash', 'file_size', 'status']

class AccessRequestForm(forms.ModelForm):
    class Meta:
        model = AccessRequest
        fields = ['file', 'requester', 'owner', 'status']
