from requests import get, post, delete, put
import pprint

pprint.pprint(put('http://localhost:5000/api/jobs/1',
                  json={'job': 'safsafsfsfsaf'}).json())  # Изменение названия
pprint.pprint(put('http://localhost:5000/api/jobs/67',
                  json={'job': 'safsafsfsfsaf'}).json())
pprint.pprint(get('http://localhost:5000/api/jobs').json())
