from django.contrib import admin
from blog.models import post
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
# admin.site.register(post)
admin.site.register(post, MarkdownxModelAdmin)
# admin.site.register(comment)
