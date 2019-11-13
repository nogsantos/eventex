# -*- coding: utf-8 -*-
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker
from eventex.core.tests import setup


class SpeakerDetailGet(TestCase):

    def setUp(self):
        self.speaker = setup.speaker()

        self.response = self.client.get(
            r('speaker_detail', slug='grace-hopper')
        )

    def test_get(self):
        """Should return status 200 when request speaker detail"""  # noqa
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Should return used template"""  # noqa
        self.assertTemplateUsed(self.response, 'core/speaker/detail.html')

    def test_html(self):
        """Should return rendered html"""  # noqa
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        """Should speaker must be in a context"""  # noqa
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailsNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(
            r('speaker_detail', slug='not-found')
        )
        self.assertEqual(404, response.status_code)
