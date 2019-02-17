from django.contrib import admin
from myblog.models import Category
from myblog.models import Post

admin.site.register(Post)
admin.site.register(Category)
