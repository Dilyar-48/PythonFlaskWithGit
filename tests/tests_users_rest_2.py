from requests import get, put, delete, post
import pprint

pprint.pprint(get('http://localhost:5000/api/v2/users').json())  # Правильный запрос на получение всех пользователей

pprint.pprint(get('http://localhost:5000/api/v2/users/1').json())  # Правильный запрос на получение одного пользователя
pprint.pprint(get('http://localhost:5000/api/v2/users/999').json())  # Запрос с неверным индексом
pprint.pprint(get('http://localhost:5000/api/v2/users/q').json())  # Запрос с буквой вместо индекса

pprint.pprint(post('http://localhost:5000/api/v2/users',
                   json={"surname": "Zam",
                         "name": "Dil",
                         "age": "15",
                         "position": "Ученик",
                         "speciality": "Школьник",
                         "address": "выфвфыавфыавыфа",
                         "email": "OOO.samaSecretnost@obmanshik.ru",
                         "hashed_password": "gfhjkm",
                         "city_from": "Москва"}).json())  # Правильный запрос
pprint.pprint(post('http://localhost:5000/api/v2/users',
                   json={"surname": "Zam",
                         "name": "Dil",
                         "age": "15",
                         "position": "Ученик"}).json())  # Нехватка аргументов
pprint.pprint(post('http://localhost:5000/api/v2/users',
                   json={'age': '155'}).json())  # Неверное значение в параметре
pprint.pprint(post('http://localhost:5000/api/v2/users', json={}).json())  # Параметры не переданы
pprint.pprint(get('http://localhost:5000/api/v2/users').json())

print(put('http://localhost:5000/api/v2/users/1', json={'surname': 'FKFDYTSUKFDYS'}).json())
print(put('http://localhost:5000/api/v2/users/2', json={'age': 27,
                                                        'address': "fdfdsfas",
                                                        'email': "scott_chief@mars.org"}).json())
pprint.pprint(get('http://localhost:5000/api/v2/users').json())

print(delete('http://localhost:5000/api/v2/users/999').json())  # Запрос с неправильным индексом
print(delete('http://localhost:5000/api/v2/users/2').json())  # Корректный запрос
print(delete('http://localhost:5000/api/v2/users/2').json())  # Попытка второй раз удалить запись
print(delete('http://localhost:5000/api/v2/users/').json())  # Пустой индекс
pprint.pprint(get('http://localhost:5000/api/v2/users').json())  # Проверка удаления
