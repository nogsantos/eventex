from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        # Nota: form.full_clean()
        # Transforma as strings recebidas do formulario em objetos
        # python de alto nivel. Ex.: A string "1" sera convertida no valor 1

        if form.is_valid():  # iternamente chama o metodo full_clean()
            html_body = render_to_string(
                'subscriptions/email.html',
                form.cleaned_data
            )
            txt_body = render_to_string(
                'subscriptions/email.txt',
                form.cleaned_data
            )
            mail.send_mail(
                subject="Subscription confirmed",
                message=txt_body,
                html_message=html_body,
                from_email="contato@eventex.com.br",
                recipient_list=[
                    'contato@eventex.com.br',
                    form.cleaned_data['email']
                ],
            )
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/subscriptions/')
        else:
            return render(request, 'subscriptions/form.html', {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/form.html', context)
