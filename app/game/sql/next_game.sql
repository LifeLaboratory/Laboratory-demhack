with
solved_question as (
select
distinct id_question
from question_history
where id_game = {id_game}
)
update game
set
    id_question = (
        select id_question from question where
        id_question != {id_question}::int
        and id_question not in (table solved_question)
        order by random () limit 1
        ),
    round = round + 1,
    point = point + coalesce({point}, 0),
    health = health + coalesce({health}),
    money = money + coalesce({money})
WHERE
id_game = {id_game}