from datetime import datetime
from django.test import TestCase
# from mock import patch

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
