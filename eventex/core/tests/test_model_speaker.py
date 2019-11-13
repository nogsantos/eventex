# -*- coding: utf-8 -*-
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker
from eventex.core.tests import setup


class SpeakerModelTest(TestCase):

    def setUp(self):
        self.speaker = setup.speaker()

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_not_required_field_description(self):
        """Field description can be blank """  # noqa
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_not_required_field_website(self):
        """Field website can be blank """  # noqa
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        """Should return an string when get the speaker object"""  # noqa
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        """Should get absolute speaker url"""  # noqa
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
