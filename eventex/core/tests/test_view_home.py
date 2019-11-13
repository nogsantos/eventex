from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_index_request_success_status_code(self):
        """Should return status code 200 when request home index"""
        self.assertAlmostEquals(200, self.response.status_code)

    def test_index_default_template(self):
        """Should render index.html as index template"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        """Should render subscription link"""
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Should show keynote speakers on home"""
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        """Should show keynote speakers link on home"""
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)
