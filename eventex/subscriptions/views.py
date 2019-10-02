from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from django.conf import settings


def subscribe(request):

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    # Nota: form.full_clean()
    # Transforma as strings recebidas do formulario em objetos
    # python de alto nivel. Ex.: A string "1" sera convertida no valor 1
    # iternamente chama o metodo full_clean()
    if not form.is_valid():
        return render(request, 'subscriptions/form.html', {'form': form})

    _send_confirmed_subscription_mail(form.cleaned_data)
    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect('/subscriptions/')


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


def new(request):
    return render(
        request,
        'subscriptions/form.html',
        {
            'form': SubscriptionForm()
        }
    )
