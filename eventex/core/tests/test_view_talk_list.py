# -*- coding: utf-8 -*-
from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Talk, Speaker, Course


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(
            title='Talk title',
            start='10:00',
            description='Talk description'
        )
        t2 = Talk.objects.create(
            title='Talk title',
            start='13:00',
            description='Talk description'
        )
        c1 = Course.objects.create(
            title='Course title',
            start='09:00',
            description='Course description',
            slots=20
        )

        speaker = Speaker.objects.create(
            name='Fabricio Nogueira',
            slug='fabricio-nogueira',
            photo='https://fabricionogueira.me/photo'
        )

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)

        self.response = self.client.get(r('talk_list'))

    def test_get(self):
        """Should list when gets"""  # noqa
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Should the list has a template"""  # noqa
        self.assertTemplateUsed(self.response, 'core/talk/list.html')

    def test_html(self):
        """Should the list has html contents"""  # noqa
        contents = [
            (2, 'Talk title'),
            (1, '10:00'),
            (1, '13:00'),
            (3, '/speakers/fabricio-nogueira/'),
            (3, 'Fabricio Nogueira'),
            (2, 'Talk description'),
            (1, 'Course title'),
            (1, '09:00'),
            (1, 'Course description')
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        """Should ensure that the list has a context"""  # noqa
        variables = ['morning_talks', 'afternoon_talks', 'courses']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)


class TalkListGetEmpty(TestCase):

    def setUp(self):
        self.response = self.client.get(r('talk_list'))

    def test_get_empty(self):
        """Should return a friendly message to user when talk list is empty"""  # noqa
        self.assertContains(
            self.response,
            'Ainda não existem palestras no período da manhã'
        )
        self.assertContains(
            self.response,
            'Ainda não existem palestras no período da tarde'
        )
