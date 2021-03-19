from app.game.provider import Provider
from app.base.helper import create_session


class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_game_info(self, data):
        game = self.provider.get_game_info(data)
        if game:
            return game[0]
        else:
            return {'error': 'Такой игры нет'}

    def send_game_answer(self, data):
        return self.provider.send_game_answer(data)

    def get_game_events(self, id_user):
        return self.provider.get_game_events(id_user)

    def execute_game_action(self, data):
        return self.provider.execute_game_action(data)

    def start_new_game(self, data):
        self.provider.end_game(data.get('id_user'))
        # Запустить игру
