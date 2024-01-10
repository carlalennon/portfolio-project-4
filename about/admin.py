from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(About)
class PostAbout(SummernoteModelAdmin):
    list_display = ('title', 'author', 'content', 'created_on')
    summernote_fields = ('content',)