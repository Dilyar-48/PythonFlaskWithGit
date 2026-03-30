from requests import get, put, delete, post
import pprint

pprint.pprint(get('http://localhost:5000/api/v2/jobs').json())

pprint.pprint(get('http://localhost:5000/api/v2/jobs/1').json())
pprint.pprint(get('http://localhost:5000/api/v2/jobs/999').json())
pprint.pprint(get('http://localhost:5000/api/v2/jobs/q').json())

pprint.pprint(post('http://localhost:5000/api/v2/jobs',
                   json={'job': 'safsafsfsfsaf',
                         'work_size': 15,
                         'collaborators': '1, 2',
                         'speciality': 'None',
                         'is_finished': True,
                         'team_leader': 1,
                         'category_id': 1}).json())
pprint.pprint(post('http://localhost:5000/api/v2/jobs',
                   json={'collaborators': '1, 2',
                         'speciality': 'None',
                         'is_finished': True,
                         'team_leader': 1}).json())  # Нехватка аргументов
pprint.pprint(post('http://localhost:5000/api/v2/jobs',
                   json={'team_leader': '1'}).json())  # Неверное значение в параметре
pprint.pprint(post('http://localhost:5000/api/v2/jobs', json={}).json())  # Аргументы не передаются
pprint.pprint(get('http://localhost:5000/api/v2/jobs').json())

print(delete('http://localhost:5000/api/v2/jobs/999').json())  # Запрос с неправильным индексом
print(delete('http://localhost:5000/api/v2/jobs/2').json())  # Корректный запрос
print(delete('http://localhost:5000/api/v2/jobs/2').json())  # Попытка второй раз удалить запись
print(delete('http://localhost:5000/api/v2/jobs/').json())  # Пустой индекс
pprint.pprint(get('http://localhost:5000/api/v2/jobs').json())  # Проверка удаления

print(put('http://localhost:5000/api/v2/jobs/1', json={'team_leader': '4'}).json())
print(put('http://localhost:5000/api/v2/jobs/2', json={'team_leader': '1',
                                                       'work_size': 100,
                                                       'category_id': 2}).json())
print(put('http://localhost:5000/api/v2/jobs/999', json={'work_size': 100}).json())  # Запрос с неправильным индексом
print(put('http://localhost:5000/api/v2/jobs/', json={'work_size': 100}).json())  # Пустой индекс
print(put('http://localhost:5000/api/v2/jobs/1', json={}).json())  # Параметры не переданы
pprint.pprint(get('http://localhost:5000/api/v2/jobs').json())
