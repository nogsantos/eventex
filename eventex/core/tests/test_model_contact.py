# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Contact, ContactTypes
from eventex.core.tests import setup


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact, self.speaker = setup.contact()

    def test_email(self):
        """Should create a contact with Email type"""
        _contact = Contact.objects.create(
            speaker=self.speaker,
            kind=ContactTypes.EMAIL,
            value='some@mail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        """Should create a contact with Phone type"""
        _contact = Contact.objects.create(
            speaker=self.speaker,
            kind=ContactTypes.PHONE,
            value='99 9 9999-9999'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choises(self):
        """Should kind be limited to only enumerate type"""
        _contact = Contact.objects.create(
            speaker=self.speaker,
            kind=100,
            value='some'
        )
        self.assertRaises(ValidationError, _contact.full_clean)

    def test_str(self):
        """Should return speaker name when get object string"""
        self.assertEqual(self.contact.value, str(self.contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        self.contact, self.speaker = setup.contact()

    def test_emails(self):
        queryset = Contact.objects.emails()
        expected = [self.contact.value]
        self.assertQuerysetEqual(queryset, expected, lambda obj: obj.value)

    def test_phones(self):
        phone_contact, _ = setup.contact(ContactTypes.PHONE)
        queryset = Contact.objects.phones()
        expected = [phone_contact.value]
        self.assertQuerysetEqual(queryset, expected, lambda obj: obj.value)
