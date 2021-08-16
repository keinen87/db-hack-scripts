from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        print("Ученика не существует, попробуйте еще раз!")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с такими данными, попробуйте указать полную ФИО!")
        return None
    return schoolkid

    