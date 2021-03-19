
import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'session'
        self.field = ['is_user', 'id_session']

    def get_game_info(self, id_user):
        self.query = f''''''
        return self.execute()[0]

    def send_game_answer(self, answer):
        self.query = f''''''
        return self.execute()[0]

    def get_game_events(self, answer):
        self.query = f''''''
        return self.execute()

    def execute_game_action(self, id_user):
        self.query = f''''''
        return self.execute()[0]

    def check_session(self, session):
        self.query = f''''''
        return self.execute()[0]
