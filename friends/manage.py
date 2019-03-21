# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:16:09 2019

@author: nkeumo
"""


from flask.cli import FlaskGroup
import datetime

from project import db, create_app
from project.models.models import FriendBook

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    """Seeds the database."""
    db.session.add(FriendBook(
        firstname = 'Tsombeng',
        lastname = 'Arnaud',
        email = 'arnaud.tsombeng@gmail.com',
        password='password',
        dateofbirth = '02/09/1990',
        gender='M',
        tell='1254863458'
        ))
    db.session.add(CurrencyData(
        firstname='justatest',
        lastname= 'testing',
        dateofbirth= '02/09/1986',
        email = 'tests@tests.com',
        password='password',
        gender='M',
        tell ='00688283',
    ))
    db.session.commit()

if __name__ == '__main__':
    cli()