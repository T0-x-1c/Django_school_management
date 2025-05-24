import os
import django

from core.models import Subject

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_mamagment.settings")

django.setup()
while True:
    print(
    "1.Додати нового студента" \
    "2.Додати новий предмет"\
    "3.Додати нового вчителя"\
    "4.Додати новий шкільний клас"\
    "5.Створити розклад"\
    "6.Додати оцінку"\
    "0.Зупинити"
        )
    choise = int(input(""))
    if choise == 0:
        break
    if choise == 2:
        name = input("Назва проекту: ")
        description = input("Опис: ")
        chek = Subject.objects.filter(name = name).first()
        if chek:
            print("Такий предмет вже існує")
        else:
            Subject.objects.create(name=name, description=description)

    if choise == 3:
        name = input("Ім'я: ")
        subject = input("предмет: ")
        chek = Subject.objects.filter(name = subject).first()
        if chek:
            print("Такий предмет вже існує")
        else:
            Subject.objects.create(name=name, description=description)