from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_index_request_success_status_code(self):
        """Should return status code 200 when request home index"""
        self.assertAlmostEquals(200, self.response.status_code)

    def test_index_default_template(self):
        """Should render index.html as index template"""
        self.assertTemplateUsed(self.response, 'index.html')
