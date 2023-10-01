from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

# Add summernote to admin blog editor and register the blog to admin panel
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


