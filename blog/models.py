from django.db import models
<<<<<<< HEAD
from django.contrib import admin

class BlogPost(models.Model):
   title = models.CharField(max_length=150)
   body = models.TextField()
   created = models.DateTimeField(auto_now_add=True)

class BlogPostAdmin(admin.ModelAdmin):
   list_display = ('title', 'created')

admin.site.register(BlogPost, BlogPostAdmin)
=======
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
>>>>>>> 58b79890669009e69b4541e50f4c72a82e7bcfff
