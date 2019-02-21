from django.contrib import admin
from myblog.models import Category
from myblog.models import Post


class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
