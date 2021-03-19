"""Работа с событиями"""

from app.base.provider import Provider

__author__ = 'Крылосов А.А.'


class Event:

    def __init__(self):
        self.db = Provider('app/event/sql')

    def insert_event(self, parameters):
        self.db.exec_by_file('insert_event.sql', parameters)
