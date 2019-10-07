from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):

    def setUp(self):
        """
        Tests initialize
        """
        self.response = self.client.get('/subscriptions/')
        self.form = self.response.context['form']

    def test_subscriptions_request_success_status_code(self):
        """Should return status code 200 when request subscriptions form"""  # noqa
        self.assertAlmostEquals(200, self.response.status_code)

    def test_form_default_template(self):
        """Should render subscriptions/form.html as subscriptions form template"""  # noqa
        self.assertTemplateUsed(self.response, 'subscriptions/form.html')

    def test_form_html_elements(self):
        """Should test required form tags"""  # noqa
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )
        # Using Subtest
        for text, cout in tags:
            with self.subTest():
                self.assertContains(self.response, text, cout)

    def test_form_csrf(self):
        """Should test required csrf markup"""  # noqa
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Should setup subscription form context"""  # noqa
        self.assertIsInstance(self.form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        """Tests initialize"""
        data = dict(
            name="Fabricio Nogueira",
            cpf="01234567891",
            email="nogsantos@mail.com",
            phone="62 9 9116-1686",
        )
        self.response = self.client.post('/subscriptions/', data)

    def test_post(self):
        """Should redirect to subscription when request is correct"""  # noqa
        self.assertEquals(302, self.response.status_code)

    def test_send_subscribe_email(self):
        """Should send a confirmation email to subscriber"""  # noqa
        # Quando em ambiente de testes, o django nao envia o email
        # anota no metodo outbox, a quantidade de emails enviados no
        # processo da requisicao
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        """Should persist a subscription"""  # noqa
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):

    def setUp(self):
        """Tests initialize"""
        self.response = self.client.post('/subscriptions/', {})

    def test_post(self):
        """Should not redirect when POST is invalid"""  # noqa
        self.assertEquals(200, self.response.status_code)

    def test_template(self):
        """Should render the template"""  # noqa
        self.assertTemplateUsed(self.response, 'subscriptions/form.html')

    def test_has_form_context(self):
        """Should render the context form on template """  # noqa
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_context_has_errors(self):
        """Should render the context form on template with errors"""  # noqa
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        """Should not persist a subscription"""  # noqa
        self.assertFalse(Subscription.objects.exists())


class SubscribeSuccessMessageTest(TestCase):

    def setUp(self):
        """Tests initialize"""
        data = dict(
            name="Fabricio Nogueira",
            cpf="01234567891",
            email="nogsantos@mail.com",
            phone="62 9 9116-1686",
        )
        # follow=True define que o redirecionamento no post seja seguido
        self.response = self.client.post('/subscriptions/', data, follow=True)

    def test_message(self):
        """Should render a success message when for is valid"""  # noqa
        self.assertContains(self.response, 'Inscrição realizada com sucesso!')
