
import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'session'
        self.field = ['is_user', 'id_session']

    def get_game_info(self, id_user):
        self.query = f'''

SELECT
  g.id_question::int4 id_question
, q.description::text description
, q.pic::text pic
, q.answer::json answer
, g.round::int4 round
, g.health::int4 health
, g.money::int4 money
, g.point::int4 point
, CASE WHEN e.id_event is not null THEN
  json_build_object('id_event', e.id_event, 'description', e.description, 'money', e.money, 'health', e.health, 'point', e.point)::json
ELSE
  json_build_object()
END as event

FROM game g
LEFT JOIN question q ON q.id_question = g.id_question
LEFT JOIN event_to_game etg ON (etg.id_game = g.id_game and etg.round >= g.round)
LEFT JOIN event e on etg.id_event = e.id_event and e.tags && q.tags
WHERE g.status = True and g.id_user = {id_user}
ORDER BY etg.id_event_to_game ASC
LIMIT 1
'''
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
