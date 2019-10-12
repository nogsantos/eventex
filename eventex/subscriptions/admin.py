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
        'paid',
        'subscription_id',
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
        'subscription_id',
    )
    # Show on rigth side a filter for list, with defined values
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

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

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = '{} inscrição foi marcada como paga.'

        if count > 1:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar selecionados como pago'


admin.site.register(Subscription, SubscriptionModelAdmin)
