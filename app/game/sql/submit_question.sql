select
  (q.answer -> {answer}::text ->> 'health')::int health_positive,
  (q.answer -> {answer}::text ->> 'point')::int point_positive,
  (q.answer -> {answer}::text ->> 'money')::int money_positive,
  (q.answer -> {answer}::text ->> 'id_event')::int id_event,
  e.health health_negative,
  e.point point_negative,
  e.money money_negative,
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