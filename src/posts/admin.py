from django.contrib import admin

from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "update", "timestamp"]
    list_filter = ["update", "timestamp"]
    list_search = ["title"]
    class Meta:
	model = Post

admin.site.register(Post, PostAdmin)
