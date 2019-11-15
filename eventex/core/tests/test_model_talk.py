# -*- coding: utf-8 -*-
from django.test import TestCase

from eventex.core.models import Talk


class TalkModelTest(TestCase):

    def setUp(self):
        self.talk = Talk.objects.create(
            title='T&acute;tulo da palestra',
            start='10:00',
            description='Descri&ccedil;&atilde;o da palestra.'
        )

    def test_create(self):
        """Should create a talk"""  # noqa
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Should the talk has speakers"""  # noqa
        self.talk.speakers.create(
            name='Fabricio Nogueira',
            slug='fabricio-nogueira',
            photo='https://fabricionogueira.me/photo'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_str(self):
        """Should return talks string"""  # noqa
        self.assertEqual(
            f'{self.talk.start} {self.talk.title}',
            str(self.talk)
        )

    def test_description_blank(self):
        """Should field description be blank"""  # noqa
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_blank(self):
        """Should field speakers be blank"""  # noqa
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_blank(self):
        """Should field start be blank"""  # noqa
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_description_null(self):
        """Should field description be null"""  # noqa
        field = Talk._meta.get_field('description')
        self.assertTrue(field.null)

    def test_start_null(self):
        """Should field start be null"""  # noqa
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)
