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
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
