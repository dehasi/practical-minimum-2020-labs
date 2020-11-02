Теперь вы уже умеете пользоваться докером. 

#### Задание
Хранить "файлы" в словаре не всегда удобно, давайте положим из в настоящий кеш.
Например в `redis`. 

Для начала, надо установите библиотеку для работы с редисом.
`pip install redis`
`pip3 install redis`
`python3 -m pip install redis`

Запустите контейнер с редисом
``` 
docker run -d -p 6379:6379  redis # довавьте остальные параметры запуска сами
```

Работать с редисом можно как со словарем, надо только подключиться

```python
import redis
cache = redis.Redis(host='0.0.0.0', port=6379, decode_responses=True)
cache.ping()
```

Теперь можно писать и читать данные
```python
key = "34"
cache.exists(key)
cache.delete(key)
cache.set(key, "value")
```

#### Задание
Теперь можно шагнуть чуть дальше и поработать с базой данных. 
В нашем случае это будет `mondodb`. 

Установите библиотеку для работы с монго
`pip install pymongo`
`python3 -m pip install pymongo`

Запустите монго
``` 
$ docker run -d -p 27017:27017 --rm mongo # довавьте остальные параметры запуска сами
```

Для работы с монго сначала надо создать клиета
```python
import pymongo
mongoClient = pymongo.MongoClient(host='0.0.0.0', port=27017)
```

потом выбрать имя базы и имя коллекции (таблицы)


```python
database =  mongoClient['hw9']
mongo_table = database['cache']
# или так
mongo_table = mongoClient['hw9']['cache']
```
Теперь, когда у нас есть коллекция(таблица) мы можем с ней работать
```python
key = "34"
value = "value"
mongo_table.insert_one({'key':key, 'value':value})
mongo_table.find_one({'key': key})
mongo_table.delete_many({'key': key})
```

На сайте монги есть [туториал](https://api.mongodb.com/python/current/tutorial.html)

#### Задание
На паттернах можно тренироваться бесконечно, 
 начать можно [тут](https://refactoring.guru/ru/design-patterns)
