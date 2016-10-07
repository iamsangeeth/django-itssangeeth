from django.db import models
from django.utils import timezone

# Create your models here.
class Messages(models.Model):
    message_id=models.AutoField(
        primary_key=True,
    )
    name=models.CharField(
        max_length=40,
        default=False,
    )
    email_id=models.CharField(
        max_length=50,
        default=False,
    )
    phone_no=models.CharField(
        max_length=12,
        default=False,
    )
    message=models.TextField(
        max_length=100,
        default=False,
    )
    time_sent=models.DateTimeField(
        default= timezone.now,
    )

    class Meta:
        ordering = ['-time_sent']
