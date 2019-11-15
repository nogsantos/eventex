from enum import IntEnum

from django.db import models
from django.shortcuts import resolve_url as r


class ContactTypes(IntEnum):
    EMAIL = 0,
    PHONE = 1,

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

    def __str__(self):
        return self.name


class Contact(models.Model):
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE,
                                verbose_name='palestrante')
    kind = models.IntegerField('tipo', choices=ContactTypes.choices(),
                               default=ContactTypes.EMAIL)
    value = models.CharField('valor', max_length=255)

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.speaker.name
