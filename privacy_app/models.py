from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=255, unique=True)
    file_size = models.IntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('archived', 'Archived'), ('deleted', 'Deleted')], default='active')

    def __str__(self):
        return self.filename

class AccessRequest(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, related_name="requester", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')], default='pending')
    request_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request for {self.file.filename} by {self.requester.username}"

class EncryptionKey(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    encrypted_key = models.CharField(max_length=512)
    issued_to = models.ForeignKey(User, related_name="issued_to", on_delete=models.CASCADE)
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Key for {self.file.filename}"
