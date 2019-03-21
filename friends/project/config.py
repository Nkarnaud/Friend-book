# customer/project/config.py
# -*- coding: utf-8 -*-
"""
Created on Sun Fev 28 21:16:09 2019

@author: nkeumo
"""
import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG_TB_ENABLED = True