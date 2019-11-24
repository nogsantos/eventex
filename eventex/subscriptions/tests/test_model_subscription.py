from datetime import datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Fabricio Nogueira',
            cpf='12345678901',
            email='nogsantos@gmail.com',
            phone='62 9 9999-9999'
        )
        self.obj.save()

    def test_create(self):
        """Should create an subscription when object is saved"""
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Should have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """Should return an instance of subscription when subscription is instanciated"""  # noqa
        self.assertEqual('Fabricio Nogueira', str(self.obj))

    def test_paid(self):
        """Should be false when created"""
        self.assertFalse(self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.subscription_id)
        self.assertEqual(url, self.obj.get_absolute_url())

    def test_ordering(self):
        """Should ensure the default list order"""
        self.assertTupleEqual(('-created_at',), Subscription._meta.ordering)
