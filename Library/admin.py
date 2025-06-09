from django.contrib import admin
from .models import Category, Posts, PostImage

# Register your models here.
class PostImageInline(admin.TabularInline): 
    model = PostImage
    extra = 1

class PostsAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(Category)
admin.site.register(Posts, PostsAdmin)
