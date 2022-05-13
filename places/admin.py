from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image
    fields = ['image', 'preview_image', 'order']
    readonly_fields = ['preview_image']
    extra = 1

    def preview_image(self, obj):
        return format_html('<img src="{}" height="200"/>', obj.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


admin.site.register(Image)
