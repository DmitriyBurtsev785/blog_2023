from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):# ссылаемся на родительский класс
    list_display = ('title', 'author')
