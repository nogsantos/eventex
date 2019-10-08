from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    # Define fields to display on list
    list_display = (
        'name',
        'cpf',
        'email',
        'phone',
        'created_at',
        'subscribed_today',
    )
    # Show on list a date navigator
    # Enable navigation by date. Pass the date fields
    date_hierarchy = 'created_at'
    # Show on list a field to query o list
    # In order, defines the search priority
    search_fields = (
        'name',
        'cpf',
        'email',
        'phone',
        'created_at',
    )
    # Show on rigth side a filter for list, with defined values
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        """
        Show a computed field on list
        """
        # now() is a function from django with considerate the timezone
        return obj.created_at.date() == now().date()

    # At this point, subscribed_today is now a parameter of class, then
    # whe can add the description injected on it
    subscribed_today.short_description = 'inscrito hoje?'
    # Show the value of subscribed_today as a grafic icon
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
