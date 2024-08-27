from django.db import models

# Create your models here.

class Application(models.Model):
    student = models.ForeignKey('user.Student', on_delete=models.CASCADE)
    specialty = models.ForeignKey('education.Specialty', on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    invoice = models.ImageField(upload_to='invoices/', null=True, blank=True)
    is_approved = models.BooleanField(default=True)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
