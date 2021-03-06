import uuid

from django.db import models
from django.shortcuts import resolve_url as r


class Subscription(models.Model):
    subscription_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    paid = models.BooleanField('pago', default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subscriptions:detail', self.subscription_id)
