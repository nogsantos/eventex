from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Should get fields form"""  # noqa
        form = SubscriptionForm()
        self.assertSequenceEqual([
            'name',
            'cpf',
            'email',
            'phone',
        ], list(form.fields))

    def test_cpf_is_valid(self):
        """Should be validate form cpf field"""
        fields = (
            ('cpf', '0123', 'length'),
            ('cpf', '012345678901', 'length'),
            ('cpf', 'ABC34567890', 'digits'),
            ('cpf', 'ABC3 567890', 'digits'),
        )
        for field, value, code in fields:
            with self.subTest():
                form = self.make_validated_form(cpf=value)
                self.assertFormErrorCode(form, field, code)

    def test_name_must_be_capitalized(self):
        """Should user name be capitalized"""
        form = self.make_validated_form(name='FABRICIO NOGUeira')
        # Cleaned data, é o dicionário que guarda todos os valores
        # do formulário já validados e sanitizados
        self.assertEqual('Fabricio Nogueira', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Should be optional when email is empty"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Should be optional when phone is empty"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Should be optional when email or phone is empty not both"""
        form = self.make_validated_form(phone='', email='')
        # __all__ is a especial errro from form. He list all error in form
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Fabricio Nogueira',
            cpf='01234567890',
            email='nogsantos@gmail.com',
            phone='62 6262626262',
        )
        data = dict(valid, **kwargs)

        form = SubscriptionForm(data)
        # Enables form validations
        form.is_valid()

        return form
