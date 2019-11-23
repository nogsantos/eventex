# -*- coding: utf-8 -*-
import random
import string

from eventex.core.models import Speaker, Contact, ContactTypes, Talk, \
    Course


def speaker() -> Speaker:
    speaker = Speaker.objects.create(
        name='Grace Hopper',
        slug='grace-hopper',
        photo='http://hbn.link/hopper-pic',
        website='http://hbn.link/hopper-site',
        description='Programadora e almirante'
    )
    return speaker


def contact(kind=ContactTypes.EMAIL) -> [Contact, Speaker]:
    name = random_str(10)
    sur_name = random_str(20)
    _speaker = Speaker.objects.create(
        name=f'{name.capitalize()} {sur_name.capitalize()}',
        slug=f'{name}-{sur_name}',
        photo=f'http://{random_str()}.com/photo/{name}',
        website=f'http://{name}-{random_str()}.com',
        description=f'{random_description(120)}'
    )

    if kind == ContactTypes.PHONE:
        _contact = Contact.objects.create(
            speaker=_speaker,
            kind=ContactTypes.PHONE,
            value='99 99999-9999'
        )
    else:
        _contact = Contact.objects.create(
            speaker=_speaker,
            kind=ContactTypes.EMAIL,
            value=f'{random_str()}@{random_str()}.com'
        )

    return _contact, _speaker


def talk():
    _talks = Talk.objects.bulk_create([
        Talk(
            title='T&acute;tulo da palestra',
            start='10:00',
            description='Descri&ccedil;&atilde;o da palestra.'
        ),
        Talk(
            title='T&acute;tulo da palestra',
            start='13:00',
            description='Descri&ccedil;&atilde;o da palestra.'
        )
    ])
    return _talks


def course():
    _course = Course.objects.create(
        title=random_str(),
        start='09:00',
        description=random_description(50),
        slots=20
    )

    return _course


def random_str(size=12, chars=string.ascii_lowercase + string.digits) -> str:
    return ''.join(random.choice(chars) for x in range(size))


def random_description(size=12) -> str:
    return '\n'.join(
        random.choice(string.ascii_letters + string.punctuation) for x in
        range(size))
