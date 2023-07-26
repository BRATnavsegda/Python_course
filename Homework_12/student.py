# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.

from subject import get_subjects_from_csv, Subject, add_subject_to_csv
from text_validator import TextValidator


class Student:

    lastname = TextValidator()
    firstname = TextValidator()
    middle_name = TextValidator()

    def __init__(self, lastname, firstname, middle_name):
        self.middle_name = middle_name
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'\n{self.lastname} {self.firstname} {self.middle_name}'

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.subjects = get_subjects_from_csv('my_file.csv')
        return instance

    def subjects_average_test_score(self) -> list[str]:
        res = []
        for sub in self.subjects:
            res.append(f'\n{sub.name} average score is {sub.average_score_on_tests()}')
        return res

    def average_grade(self):
        sum_ = 0
        count = 0
        for sub in self.subjects:
            for item in sub.grades:
                sum_ += item
                count += 1
        return f'\nThis student average grade is {sum_ / count}'


if __name__ == '__main__':
    s = Student('Череззаборногузадирищенко', 'Гучапундра', 'Вылысыпыдыстовна')
    print(s)
    print(*s.subjects_average_test_score())
    print(s.average_grade())
