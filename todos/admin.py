from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'datetime_created', 'datetime_updated', 'is_completed']
    list_editable = ['author']
    raw_id_fields = ['author']
    list_filter = ['author', 'is_completed']


admin.site.register(Todo, TodoAdmin)
