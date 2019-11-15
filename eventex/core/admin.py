from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact


class ContactInLine(admin.TabularInline):
    """
    Cria no formulário, uma lista que permite adionar n valores relacionados.
    """
    model = Contact
    extra = 1  # Define a quantidade inicial de valores apresentados, default 3.


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]

    # Enable to from a field, fill another with javascript
    # This field is a dictionary.
    # Params:
    #   1. Field name to be populated
    #   2. The value is, the target field, will be read to get value
    prepopulated_fields = {'slug': ('name',)}

    # Values to display on list
    list_display = ['photo_img', 'name', 'website_link']

    def website_link(self, obj):
        return format_html(
            '<a target="_blank" href="{0}">{0}</a>',
            obj.website
        )

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html(
            '<img width="32" src="{}" alt="{}" />',
            obj.photo,
            obj.name
        )

    photo_img.short_description = 'foto'


admin.site.register(Speaker, SpeakerModelAdmin)
