from unittest import TestCase
from app.event.event import Event
from app.game.game import Game

class TestDev(TestCase):

    def test_dev(self):
        Event().insert_event({
            'description': 'test',
            'id_session': 'test',
            'tags': ['test_tag', 'tast']
        })

    def test_start(self):
        Game().start_game({
            'id_user': 1,
            'id_person': 1
        })

    def test_submit_question(self):
        Game().submit_question({
            'answer': 0,
            'id_user': 1
        })
