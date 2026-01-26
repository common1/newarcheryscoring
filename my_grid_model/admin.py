from django.contrib import admin

from .models import SimpleGrid

@admin.register(SimpleGrid)
class SimpleGridAdmin(admin.ModelAdmin):
    list_display = ('name',)

