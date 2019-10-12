from django.test import TestCase
from unittest.mock import Mock

from eventex.subscriptions.admin import SubscriptionModelAdmin
from eventex.subscriptions.admin import Subscription
from eventex.subscriptions.admin import admin


class SubscriptionModelAdminTest(TestCase):

    def setUp(self):
        Subscription.objects.create(
            name='Fabricio Nogueira',
            cpf='01234567890',
            email='nogsantos@gmail.com',
            phone='62 626262626262'
        )

        self.queryset = Subscription.objects.all()
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action marked as paid should be installed"""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """Should mark as paid when itens are selected"""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        mock = self.call_action()
        mock.assert_called_once_with(
            None, '1 inscrição foi marcada como paga.'
        )

    def call_action(self):

        # Manteins the original object (Is realy necessary?)
        # old_message_user = SubscriptionModelAdmin.message_user

        # Mock
        mock = Mock()
        SubscriptionModelAdmin.message_user = mock
        self.model_admin.mark_as_paid(None, self.queryset)

        # Restore object reference (Is realy necessary?)
        # SubscriptionModelAdmin.message_user = old_message_user

        return mock
