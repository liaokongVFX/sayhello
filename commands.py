# -*- coding: utf-8 -*-
# Time    : 2019/4/22 21:46
# Author  : LiaoKong

import click

from models import Message
from ext import db


def forge(count):
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo("Working...")

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )

        db.session.add(message)

    db.session.commit()

    click.echo("Created %d fake messages." % count)


forge(50)
