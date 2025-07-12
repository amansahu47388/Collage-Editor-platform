from django.contrib import admin
from .models import Collage, ImageItem

class ImageItemInline(admin.TabularInline):
    model = ImageItem
    extra = 1

class CollageAdmin(admin.ModelAdmin):
    inlines = [ImageItemInline]
    list_display = ('title', 'created_at')
    search_fields = ('title',)

admin.site.register(Collage, CollageAdmin)
