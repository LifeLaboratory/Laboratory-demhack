from app.game.provider import Provider
from app.base.helper import create_session
from app.game.game import Game


class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_game_info(self, data):
        game = self.provider.get_game_info(data)
        if game:
            if isinstance(game[0].get('event'), dict):
                self.provider.delete_event_to_game(game[0].get('event').get('id_event_to_game'))
                game[0].get('event').pop('id_event_to_game')
            return game[0]
        else:
            return {'error': 'Такой игры нет'}

    def send_game_answer(self, data):
        Game().submit_question(data)
        return self.get_game_info(data)

    def get_game_events(self, id_user):
        return self.provider.get_game_events(id_user)

    def execute_game_action(self, data):
        return self.provider.execute_game_action(data)

    def start_new_game(self, data):
        self.provider.end_game(data.get('id_user'))
        Game().start_game(data)
        return self.get_game_info(data)
