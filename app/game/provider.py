
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

    def end_game(self, id_user):
        """
        Метод для завершения всех игр пользователя
        :param id_user:
        :return:
        """
        self.query = f'''
update game
set status = false
where id_user = {id_user}
  and status is true
        '''
        return self.execute()
