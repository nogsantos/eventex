from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/form.html', context)
