# -*- coding: utf-8 -*-
from django.db import models

"""
class EmailContactManager(models.Manager):

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(kind=0)
        return queryset


class PhoneContactManager(models.Manager):

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(kind=1)
        return queryset
"""


class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


"""
class KindContactManager(models.Manager):
    def get_queryset(self):
        return KindQuerySet(self.model, using=self._db)

    def emails(self):
        return self.get_queryset().emails()

    def phones(self):
        return self.get_queryset().phones()
"""


class PeriodManager(models.Manager):
    MIDDAY = '12:00'

    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY)
