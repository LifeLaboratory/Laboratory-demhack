select
  (q.answer -> {answer}::text ->> 'health')::int health,
  (q.answer -> {answer}::text ->> 'point')::int point,
  (q.answer -> {answer}::text ->> 'money')::int money,
  e.round event_round,
  g.round cur_round,
  g.id_game,
  e.id_event
from
  game g

join question q on q.id_question = g.id_question
left join event e on e.id_event = (q.answer -> 0::text ->> 'id_event')::int
where
  id_user = {id_user}
and status is true