from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):

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
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_form_csrf(self):
        """Should test required csrf markup"""  # noqa
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Should setup subscription form context"""  # noqa
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_form_has_fields(self):
        """Should get fields form"""  # noqa
        self.assertSequenceEqual([
            'name',
            'cpf',
            'email',
            'phone',
        ], list(self.form.fields))
