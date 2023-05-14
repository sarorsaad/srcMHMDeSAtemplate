from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Customize the admin interface if needed
    pass

admin.site.register(Post, PostAdmin)

