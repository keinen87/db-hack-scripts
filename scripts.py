import random
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


def fix_marks(name):
    schoolkid = get_schoolkid(name)
    if schoolkid:
        negative_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
        if negative_marks:
            for negative_mark in negative_marks:
                negative_mark.points = random.choice((4,5))
                negative_mark.save()
            print("Оценки исправлены!") 
        else:
            print("У ученика нет плохих оценок!")


def remove_chastisements(name):
    schoolkid = get_schoolkid(name)
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        if chastisements:
            chastisements.delete()
            print("Замечания удалены!")
        else:
            print("У ученика нет замечаний!")
        
            