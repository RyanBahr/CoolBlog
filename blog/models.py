from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class post(models.Model):
    """ A model representing a post to this blog."""
    title = models.CharField(max_length=32)
    content = MarkdownxField()
    published_on = models.DateField()
    class Meta:
        ordering = ['-published_on']

    def formatted_markdown(self):
        return markdownify(self.content)

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('blogpost', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'title'

# class pdf(models.Model):
#     title = models.CharField(max_length=64)
#     embed = models.CharField(max_length=256)
#
#     def get_absolute_url(self):
#         """Returns the url to access a particular post instance."""
#         return reverse('pdf', args=[str(self.id)])


# class comment(models.Model):
#     post = models.ForeignKey('blog.post', on_delete=models.CASCADE, related_name='comments')
#     author = models.CharField(max_length=200)
#     text = MarkdownxField()
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.text

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
