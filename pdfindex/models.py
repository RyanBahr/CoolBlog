from django.db import models
from django.urls import reverse

# Create your models here.
class pdf(models.Model):
    title = models.CharField(max_length=32)
    embed_url = models.CharField(max_length=1000)
    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        """Returns the url to access a particular pdf instance."""
        return reverse('pdfdetail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'title'
