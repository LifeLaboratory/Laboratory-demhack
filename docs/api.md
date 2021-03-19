# API:
### Работа с пользователем
```python
-> GET /api/user # получение списка пользователей
response:
{
  'users': [
    {
      'id_user': int,
      'login': str
    }
  ]
}

-> GET /api/user/profile  # получение своего профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'count_game': int,  # Количество игр
  'max_point': int,  # Максимальное количество очков
  'pic': str,
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'health': int,   # Здоровье
      'money': int,    # Деньги
      'point': int # Количество очков, заработанных за игру.
    }
  ]
}

-> GET /api/user/<int:id_user> # получение профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'count_game': int,  # количество игр
  'max_point': int,  # Максимальное количество очков
  'pic': str,
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'health': int,   # Здоровье
      'money': int,    # Деньги
      'point': int # Количество очков, заработанных за игру.
    }
  ]

}

-> POST /api/user/login # авторизация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}

-> POST /api/user/register #  регистрация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}
```

### Выбор персонажа
```python
-> GET /api/person # Список персонажей в игре
response:
{
  'id_person': int,
  'name': str,
  'description': str, # описание персонажа
  'pic': str, # ссылка на картинку
  'health': int,  # Здоровье
  'money': int,    # Деньги
  'value': int,  # количество денег
}
```

### Рейтинг
```python
-> GET /api/rating # Рейтинг игр пользователей
response:
{
    'top': [
        {
            'id': int,            # - номер в рейтинге
            'point': int,         # - количество баллов
            'health': int,        # - кол-во жизней
            'money': int,         # - кол-во денег
            'round': int,         # - на каком раунде проиграл
            'id_user': int,       # - Идентификатор юзера, для перехода в его профиль (не выводить)
            'user_name': str,     # - имя пользователя
            'user_pic': str,      # - Картинка юзера пока не выводить
            'person_name': str,   # - Имя героя за которого играл
            'person_descr': str,  # - Описание героя
            'person_pic': str     # - Изображение героя
        }
    ]
}
```

### Игра
```python
-> GET /api/game # Получить данные о текущей игре
response:
{
  'id_question': int,
  'description': str,
  'answer': [
    { 
      'id': int,
      'description': text,
      'health': int,   # Здоровье
      'point': int, # количество очков
      'money': int, # количество денег
    },
  ]
  'round': int, # Номер раунда игры
  'health': int,   # Здоровье
  'money': int,    # Деньги
  'point': int, # количество очков
}

-> POST /api/game # Запуск новой игры
{
  'id_person': int # идентификатор персонажа, с которым начинается игра
}

-> POST /api/game/question
{
  'answer': str # левый или правый ответ 
}
response 
{
  'id_question': int,
  'description': str,
  'left_answer': str,  # Первый ответ
  'right_answer': str,  # Второй ответ
  'round': int, # Номер раунда игры
  'health': int,   # Здоровье
  'money': int, # количество денег
  'point': int, # количество очков
}

GET /api/game/events # Получить события, которые произошли в игре
response 
{
  'event': [
    {
      'element': str, # какой элемент изменился
      'description': str # какое сообщение вывести
    }
  ]
}


-> POST /api/game/action # Выполнить действие
{
  'action': str # worked/call_friend/call_delivery
}
response:
{
  'id_question': int,
  'description': str,
  'left_answer': str,  # Первый ответ
  'right_answer': str,  # Второй ответ
  'round': int, # Номер раунда игры
  'health': float,   # Здоровье
  'money': int, # количество денег
  'point': int, # количество очков
}

```
