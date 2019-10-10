from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import resolve_url as r

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(
        request,
        'subscriptions/form.html',
        {
            'form': SubscriptionForm()
        }
    )


def create(request):
    form = SubscriptionForm(request.POST)

    # Nota: form.full_clean()
    # Transforma as strings recebidas do formulario em objetos
    # python de alto nivel. Ex.: A string "1" sera convertida no valor 1
    # iternamente chama o metodo full_clean()
    if not form.is_valid():
        return render(request, 'subscriptions/form.html', {'form': form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    # @todo: Fix to use model value
    _send_confirmed_subscription_mail(form.cleaned_data)

    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect(
        r('subscriptions:detail', subscription.subscription_id)
    )


def _send_confirmed_subscription_mail(context):
    html_body = render_to_string(
        'subscriptions/email.html',
        context
    )
    txt_body = render_to_string(
        'subscriptions/email.txt',
        context
    )
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
