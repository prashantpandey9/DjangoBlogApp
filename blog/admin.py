from django.contrib import admin

# Register your models here
from .models import Post

admin.site.register(Post)
admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to Blog Portal"
