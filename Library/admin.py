from django.contrib import admin
from .models import Category, Author, Posts

# Register your models here.
admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(Author)