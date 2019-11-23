from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact, Talk, Course


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
    list_display = ['photo_img', 'name', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return format_html(
            '<a target="_blank" href="{0}">{0}</a>',
            obj.website
        )

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html(
            '<img width="32" src="{}" alt="{}" />',
            obj.photo,
            obj.name
        )

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'Email'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'phone'


class TalkModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(course=None)


"""Register the models on admin"""
admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)
