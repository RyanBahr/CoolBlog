from django.db import models
from django.urls import reverse

class post(models.Model):
    """ A model representing a post to this blog."""
    title = models.CharField(max_length=32)
    content = models.TextField()
    published_on = models.DateField()
    class Meta:
        ordering = ['-published_on']

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('blogpost', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return title

# class Author(models.Model):
#     """Model representing an author/user of this blog."""
#     username = models.CharField(max_length=100)
#
#     class Meta:
#         ordering = ['username']
#
#     def get_absolute_url(self):
#         """Returns the url to access a particular author instance."""
#         return reverse('author-detail', args=[str(self.id)])
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return f'username'
