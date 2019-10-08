from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        """
        Tests initialize
        """
        self.obj = Subscription.objects.create(
            subscription_id='241c7891-0df5-4dbf-8c76-5c75d274b782',
            name='Fabricio Nogueira',
            cpf='01234567891',
            email='nogsantos@mail.com',
            phone='62 9 9116-1686',
        )
        self.response = self.client.get(
            '/subscriptions/{}/'.format(self.obj.subscription_id))

    def test_get(self):
        """Should return status code 200 when request subscriptions detail"""  # noqa
        self.assertAlmostEquals(200, self.response.status_code)

    def test_template(self):
        """Should render subscriptions/detail.html as subscriptions detail template"""  # noqa
        self.assertTemplateUsed(self.response, 'subscriptions/detail.html')

    def test_context(self):
        """Should get context"""  # noqa
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone,
        )

        # Using Subtest
        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/subscription/0/')
        self.assertEqual(404, response.status_code)
