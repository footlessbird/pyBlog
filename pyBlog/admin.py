from django.contrib import admin
from .models import Post

# localhost:8000/admin에 Post 등록
admin.site.register(Post)
