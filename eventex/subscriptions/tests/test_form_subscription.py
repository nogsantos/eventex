from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        """Tests initialize"""
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Should get fields form"""  # noqa
        self.assertSequenceEqual([
            'name',
            'cpf',
            'email',
            'phone',
        ], list(self.form.fields))
