from django.contrib import admin

from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created')
    list_display_links = ('pk',)
    search_fields =  ('title',)
    list_filter = ('created',)