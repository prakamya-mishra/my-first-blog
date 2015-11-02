from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
   title = models.CharField(max_length=150)
   body = models.TextField()
   created = models.DateTimeField(auto_now_add=True)

class BlogPostAdmin(admin.ModelAdmin):
   list_display = ('title', 'created')

admin.site.register(BlogPost, BlogPostAdmin)
