from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    """The validate method receive a callable list passing only
        the value and raise an exception when validator has error"""

    if not value.isdigit():
        # the second param is the validation code
        raise ValidationError('CPF deve conter apenas numeros', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 digitos', 'length')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        """
        Método especial.
        O formulário procura por qualquer método 'clean_' e um nome de um campo existente
        e o utiliza como uma espécie de hook, um complemento da validação em sí.
        É uma alternativa que possibilita a extensão do processo de validação.

        In [1]: from eventex.subscriptions.forms import SubscriptionForm
        In [2]: valid = dict(
        ...:             name='Fabricio Nogueira',
        ...:             cpf='01234567890',
        ...:             email='nogsantos@gmail.com',
        ...:             phone='62 6262626262',
        ...:         )
        In [3]: form = SubscriptionForm(dict(valid, name='FABRICIO NOGUeira'))
        In [4]: form.is_valid()
        Out[4]: True
        In [5]: form.cleaned_data
        Out[5]:
        {'name': 'Fabricio Nogueira',
        'cpf': '01234567890',
        'email': 'nogsantos@gmail.com',
        'phone': '62 6262626262'}
        """  # noqa

        # O método é chamado após o cleaned_data, desse forma,
        # já existirá um valor associado ao campo.
        name = self.cleaned_data.get('name')

        words = (w.capitalize() for w in name.split())
        return ' '.join(words)

    def clean(self):
        """
        Especial method.
        The clean method is called after all fields was validated, after cleaned_data is fully filled.
        On form, this is the moment when we can evaluate and manipulate all fields in the form
        """  # noqa

        if (not self.cleaned_data.get('email') and
                not self.cleaned_data.get('phone')):

            raise ValidationError('Informe seu e-mail ou telefone')

        # After validations, it's important return the cleaned_data!
        return self.cleaned_data
