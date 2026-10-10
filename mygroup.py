# -*- coding: utf-8 -*-

# Список студентов группы: имя, фамилия, экзамены, оценки
groupmates = [
    {
        "name": "Б.",
        "surname": "Алексеев",
        "exams": ["Информатика", "ЭЗИС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "И.",
        "surname": "Алтухов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "А.",
        "surname": "Васильева",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "А.",
        "surname": "Григорян",
        "exams": ["Математика", "Физика", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Л.",
        "surname": "Дмитроченко",
        "exams": ["Информатика", "История", "АиГ"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Д.",
        "surname": "Ерёмин",
        "exams": ["Философия", "Математика", "Web"],
        "marks": [5, 5, 4]
    },
]


def print_students(students):
    """Выводит список студентов в виде таблицы."""
    print(u"Фамилия".ljust(15), u"Имя".ljust(12),
          u"Экзамены".ljust(35), u"Оценки".ljust(20))
    for student in students:
        print(student["surname"].ljust(15),
              student["name"].ljust(12),
              str(student["exams"]).ljust(35),
              str(student["marks"]).ljust(20))


def average_mark(student):
    """Средний балл одного студента."""
    return sum(student["marks"]) / len(student["marks"])


def filter_by_average(students, threshold):
    """Возвращает список студентов со средним баллом ВЫШЕ порога."""
    result = []
    for student in students:
        if average_mark(student) > threshold:
            result.append(student)
    return result


# --- Основная программа ---
if __name__ == "__main__":
    print("Все студенты группы:")
    print_students(groupmates)

    # Ввод порога с клавиатуры
    threshold = float(input("\nВведите минимальный средний балл: "))

    filtered = filter_by_average(groupmates, threshold)

    print("\nСтуденты со средним баллом выше", threshold, ":")
    if filtered:
        print_students(filtered)
    else:
        print("Нет таких студентов.")