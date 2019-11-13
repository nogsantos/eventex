# -*- coding: utf-8 -*-
from eventex.core.models import Speaker


def speaker() -> Speaker:
    speaker = Speaker.objects.create(
        name='Grace Hopper',
        slug='grace-hopper',
        photo='http://hbn.link/hopper-pic',
        website='http://hbn.link/hopper-site',
        description='Programadora e almirante'
    )
    return speaker
