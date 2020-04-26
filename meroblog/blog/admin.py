from django.contrib import admin
from . import models


@admin.register(models.Blog)
class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'status', 'date', 'category']
    search_fields = ['title', 'status', 'date', 'category']

@admin.register(models.MainMenu)
class AdminMainMenu(admin.ModelAdmin):
    list_display = ['name', 'status', 'title', 'posted_by' ]
    search_fields = ['name', 'title','posted_by', 'posted_at']
    prepopulated_fields = {'slug' :('title',)}
    date_hierarchy = 'created_at'