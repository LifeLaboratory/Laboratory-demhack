update game
set
    id_question = (select id_question from question order by random () limit 1),
    round = round + 1,
    point = point + coalesce({point}, 0)),
    healt = healt + coalesce({healt}),
    money = money + coalesce({money})
WHERE
id_game = {id_game}