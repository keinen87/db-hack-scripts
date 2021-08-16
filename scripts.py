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


def add_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    if schoolkid:
        commendations = [
            'Молодец!',
            'Отлично!',
            'Хорошо!',
            'Гораздо лучше, чем я ожидал!',
            'Ты меня приятно удивил!',
            'Великолепно!',
            'Прекрасно!',
            'Ты меня очень обрадовал!',
            'Именно этого я давно ждал от тебя!',
            'Сказано здорово – просто и ясно!',
            'Ты, как всегда, точен!',
            'Очень хороший ответ!',
            'Талантливо!',
            'Ты сегодня прыгнул выше головы!',
            'Я поражен!',
            'Уже существенно лучше!',
            'Потрясающе!',
            'Замечательно!',
            'Прекрасное начало!',
            'Так держать!',
            'Ты на верном пути!',
            'Здорово!',
            'Это как раз то, что нужно!',
            'Я тобой горжусь!',
            'С каждым разом у тебя получается всё лучше!',
            'Мы с тобой не зря поработали!',
            'Я вижу, как ты стараешься!',
            'Ты растешь над собой!',
            'Ты многое сделал, я это вижу!',
            'Теперь у тебя точно все получится!'
        ]    
        lesson = Lesson.objects.filter(
            year_of_study=6,
            group_letter='А',
            subject__title=subject).first()
        if lesson:
            Commendation.objects.create(
                schoolkid=schoolkid,
                created=lesson.date,
                subject=lesson.subject,
                teacher=lesson.teacher,
                text=random.choice(commendations)
            )
            print("Похвала добавлена!")    