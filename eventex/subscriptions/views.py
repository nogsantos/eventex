from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.generic.base import View

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionCreate(View):
    template_name = 'subscriptions/form.html'
    form_class = SubscriptionForm

    def get(self, *args, **kwargs):
        return self._render_to_response({'form': self.get_form()})

    def post(self, *args, **kwargs):
        form = self.get_form()

        if not form.is_valid():
            return self._render_to_response({'form': form})

        subscription = Subscription.objects.create(**form.cleaned_data)

        self._send_confirmed_subscription_mail(form.cleaned_data)

        messages.success(self.request, 'Inscrição realizada com sucesso!')
        return HttpResponseRedirect(subscription.get_absolute_url())

    def get_form(self):
        if self.request.method == 'POST':
            return self.form_class(self.request.POST)
        return self.form_class()

    def _render_to_response(self, context):
        return render(self.request, self.template_name, context)

    def _send_confirmed_subscription_mail(self, context):
        template = 'subscriptions/email'
        html_body = render_to_string(f'{template}.html', context)
        txt_body = render_to_string(f'{template}.txt', context)
        mail.send_mail(
            subject="Subscription confirmed",
            message=txt_body,
            html_message=html_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[
                settings.DEFAULT_FROM_EMAIL,
                context['email']
            ],
        )


new = SubscriptionCreate.as_view()


def detail(request, subscription_id):
    try:
        subscription = Subscription.objects.get(
            subscription_id=subscription_id
        )
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/detail.html', {
        'subscription': subscription
    })
