# Скрипты для правки базы данных электронного дневника

[Репозиторий электронного дневника](https://github.com/devmanorg/e-diary)

## Как пользоваться

Положите файл `scripts.py` в корень проекта, а потом зайдите в `shell`. Для этого в командной строке запустится интерактивная консоль Python, при этом сразу подключится Django:

```bash
$ python manage.py shell
Python 3...
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```
Импортируйте сперва модуль random и модели(можно скопировать и вставить из файла scripts.py), а потом сами функции: 

```python
>>> import random
>>> from datacenter.models import Schoolkid, Lesson, Mark, Сhastisement, Commendation
>>> from scripts.py import get_schoolkid, fix_marks, remove_chastisements, add_commendation
```

## Исправление оценок на пятёрки

Функция `fix_marks` правит плохие оценки, двойки или тройки на пятерки.
Принимает на вход данные ученика:

```python
>>> fix_marks('Афдеева Екатерина')
Ученика не существует, попробуйте еще раз!
```

В случае успеха:


```python
>>> fix_marks('Авдеева Екатерина')
Оценки исправлены!
```

## Удаление всех замечаний

Функция `remove_chastisements` удаляет все замечания.
Принимает на вход данные ученика:

```python
>>> remove_chastisements('Авдеева Екатерина')
Замечания удалены!
```

## Добавление похвалы ученику из 6А

Функция `add_commendation` добавляет похвалу ученику по определенному предмету.
Принимает на вход имя ученика и предмет по которому добавится благодарность:

 ```python
>>> add_commendation('Тетерин Орест','Технология')
Похвала добавлена!
 ```

*Обратите внимание, что в 6 классе предметов меньше чем в более старших классах.*