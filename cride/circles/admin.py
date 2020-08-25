# Django
from django.contrib import admin

# Models
from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit'
    )
    search_field = ('slug_name', 'name')
    list_filter = ('is_public', 'verified', 'is_limited')