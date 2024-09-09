from django.db import models
from localflavor.us.models import USPostalCodeField



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    postal_code = USPostalCodeField(max_length=10, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['author'], name='author_idx'),
        ]

