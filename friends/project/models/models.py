# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:16:09 2019

@author: nkeumo
"""

import datetime
from flask import current_app
from project import db, bcrypt

class FriendBook(db.Model):
    __tablename__ = "friends"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128))
    dateofbirth = db.Column(db.DateTime)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    gender = db.Column(db.String(128))
    tell = db.Column(db.String(128))


    def __init__(self, firstname, lastname, dateofbirth, email, password, gender, tell):
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = datetime.datetime.strptime(
            dateofbirth, "%d/%m/%Y").date()
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.gender = gender
        self.tell = tell

    def to_json_friends(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'date_of_birth': self.dateofbirth,
            'email': self.email,
            'gender': self.gender,
            'tell': self.tell
        }