from django.shortcuts import render, redirect
from .forms import FileUploadForm, AccessRequestForm
from .models import File, AccessRequest, EncryptionKey
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user  # Assign the current logged-in user as the file owner
            file.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'privacy_app/upload_file.html', {'form': form})

@login_required
def request_access(request, file_id):
    file = File.objects.get(id=file_id)
    if request.method == 'POST':
        access_request = AccessRequest(file=file, requester=request.user, owner=file.user)
        access_request.save()

        # Send a notification to the file owner (you can use Django's email functionality here)
        send_mail(
            'File Access Request',
            f'{request.user.username} has requested access to your file {file.filename}.',
            settings.EMAIL_HOST_USER,
            [file.user.email],
        )

        return redirect('file_list')
    return render(request, 'privacy_app/request_access.html', {'file': file})

@login_required
def approve_request(request, request_id):
    access_request = AccessRequest.objects.get(id=request_id)
    if access_request.owner == request.user:
        access_request.status = 'approved'
        access_request.approval_date = timezone.now()
        access_request.save()

        # Generate and send a secret key (encrypted) to the requester via email
        encryption_key = EncryptionKey(file=access_request.file, owner=request.user, encrypted_key="encrypted_secret_key", issued_to=access_request.requester)
        encryption_key.save()

        send_mail(
            'File Access Approved',
            f'Your request for file {access_request.file.filename} has been approved. Use the following key to decrypt the file.',
            settings.EMAIL_HOST_USER,
            [access_request.requester.email],
        )

        return redirect('file_list')
    return redirect('file_list')
