from django.contrib import admin
from .models import Thread, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Thread)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content', 'tags']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)