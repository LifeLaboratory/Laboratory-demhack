# Структуруа базы данных

### Пользователь
```sql
  'id_user': str,
  'login': str,
  'password': str,
  'pic': str # Ссылка на картинку
```

### Игра
```sql
  'id_game': int,
  'id_user': int,
  'id_question': int,
  'time_open': timestamp,
  'time_close': timestamp,
  'round': int, # Номер раунда игры
  'health': float,   # Здоровье
  'point': int, # количество очков
  'money': int, # количество денег
  'id_person': int,
```


### Вопросы
```sql
  'id_question': int,
  'description': text,
  'pic': text, # Ссылка на картинку
  'answer': [
    {
      'text': text,
      'health': float,   # Здоровье
      'point': int, # количество очков
      'money': int, # количество денег
    },
  ],
  'tags': text[]
```


### Персонажи
```sql
  'id_person': int,
  'name': str,
  'description': str, # описание персонажа
  'health': float,
  'money': int,
  'point': int,
  'pic': str # ссылка на картинку
```


### Сессии пользователей
```sql
  'id_user': int,
  'id_session': text
```


### События
```sql
  'id_event': int,
  'description': text,
  'health': float,
  'money': int, # Количество денег
  'point': int, # Количество очков
  'tags': text[]
```

### Связь 

```sql
  'id_event': int,
  'id_game': int,
  'round': int
```