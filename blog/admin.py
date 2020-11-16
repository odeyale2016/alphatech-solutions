from django.contrib import admin
from blog.models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date')
    
admin.site.register(Post, PostAdmin)
