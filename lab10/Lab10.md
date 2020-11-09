#### Задание
Давайте научимся писать юнит-тесты


Начать можно с ключевого слова `assert` в питоне.

Работает это так, мы передаем условие (булево выражение) и если оно ложно 
то выбрасывается исключение с указанным сообщением.

Запустите пример и убедитесь сами
```python
assert 1 > 2, "Сообщение об ошибке"
```

Теперь вы можете, например проверять коррекность входных данных.

Например
```python
def sqrt(x):
    assert x > 0, f'x must be positive, but was: {x}'
```

Давайте напишем простейший класс, чтобы былона чем тренироваться

```
cat my_math.py
def inc(x):
    return x + 1
```

Давайте напишем на него тест. 
Т.к. продакшн код не должен вообще ничего знать не про какие тесты,
то создадим отдельный файл `test_my_math.py` (в домашке, возможно придется создать отдельную папку для тестов)

Создадим там класс
```
class MyTestCase(unittest.TestCase):
```

По конвенции `pytest`, имена всех тестовых методов должны начинаться с `test_`

Давайте создадим такой метод

```python
def test_answer(self):
    assert inc(3) == 4
``` 

теперь можно выполнить `pytest` и увидеть результат

``` 
$ pytest
======================= test session starts ==============================
platform darwin -- Python 2.7.16, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
rootdir: /Users/ravil/experimental/csc-course/texts/lec10/lab
collected 2 items

test_my_math.py ..                                                                                                                                                                                 [100%]
===================== 2 passed in 0.02 seconds ============================

```
Не забудьте создать файл `__init__.py` с рабочей и родительской директории.

Использовать `assert` не всегда бывает удобно. Поэтому у `pytest` есть свои "ассершены"

```
self.assertEqual(inc(1), 2)
```

Теперь вы можете тестировать свои функции и методы.

Подробнее можно почитать [тут](https://docs.pytest.org/en/stable/)

#### Задание
Но что если класс зависит от других классов. Например наш сервис зависит от репозиториев.
Мы не хотим тестировать репозитории, мы хотим убедиться, что сервис вызывает методы репозитория с правильными параметрами.
Например если мы делаем `get`, то сервис идет с монгу, а не в редис.  

Для этого существуют тест-двойники (фэйки, стабы, моки). Давайте "замокаем" репозитории и проверить что сервис вызывает нужный

Добавляем нужные импорты
```python
from mock import MagicMock
```

Создаем сервис и подкладываем моки
```python
def setUp(self):
    self.cache = MagicMock()
    self.service = Service(self.cache, MagicMock())
```

Тестируем
```python
def test_get_calls_mongo(self):
    key = "key"
    self.cache.exists.return_value = True # говорим моку вернуть True, при вызове exists

    self.service.get(key)

    self.cache.get.assert_called_with(key) # проверяем, что элемент был взят из кеша
```

Примеры можно нагуглить по запросу `pytest mock`

#### Задание
Итак, мы умеем писать юнит-тесты и мокать зависимости. Но что если мы хотим потестить интеграцию.
Например, что наш контроллер действительно принимает http запросы?

Тут нам поможет фласк, у него есть `test_client`.

Для этого нам надо сказать фласку, что мы будем его тестировать

```python
def setUp(self):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False

    self.app = app.test_client()
    self.assertEqual(app.debug, False)
```

Теперь можно тестировать

```python
def test_delete_returns204(self):
    response = self.app.delete('/storage/1', follow_redirects=True)

    self.assertEqual(response.status_code, 204)
```

#### Задание
Как убедиться что балансировщик высылает правильные http запросы?

Воспользуемся библиотекой [responses](`https://github.com/getsentry/responses`)

Для начала, раз у нас фласк то придется сделать такой же сетап
```python
def setUp(self):
    # то же самое что и в прошлом задании
```

Теперь можно "мокать" http-ответы
```python
responses.add(responses.GET, 'http://localhost:8080/storage/11', json={'value': 'value'}, status=200)
```
И проверять, что на "замоканный" url, действительно приходил запрос

```python
assert responses.calls[0].request.url == 'http://localhost:8080/storage/11
``` 

#### Задание
Раз мы делаем интеграционные тесты, то можно проверить что репозиторий умеет работать с монго или редисом.

А значит мы можем поднять редис
```python
def setUp(self):
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    self.cache = RedisRepository(redis_client)
    os.system('docker run --rm --detach --name rediska-test --publish 6379:6379 redis')
```

Выполнить наш тест
```python
def test_get_returns_value_from_cache(self):
    self.cache.put("key", "value")

    value = self.cache.get("key")

    self.assertEqual(value, "value")
```

И "потушить" редис

```
def tearDown(self):
    os.system('docker stop rediska-test')
```

Но такие тесты (с использованием докера или внешних сервисов) долгие и ресурсоемкие, 
поэтому по возможности, стоит использовать юнит-тесты 
