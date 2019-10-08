from django.core import mail
from django.test import TestCase


class SubscribeMailBody(TestCase):
    def setUp(self):
        """Tests initialize"""
        data = dict(
            name="Fabricio Nogueira",
            cpf="01234567891",
            email="nogsantos@mail.com",
            phone="62 9 9116-1686",
        )
        self.client.post('/subscriptions/', data)
        # O object autbox guarda uma lista dos emails enviados
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Subscription confirmed'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'nogsantos@mail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fabricio Nogueira',
            '01234567891',
            'nogsantos@mail.com',
            '62 9 9116-1686',
        ]

        # Using Subtest
        with self.subTest():
            for content in contents:
                self.assertIn(content, self.email.body)
