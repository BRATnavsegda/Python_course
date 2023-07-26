# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета
import csv
from int_validator import IntValidator
from text_validator import TextValidator


class Subject:
    name = TextValidator()
    grades = IntValidator(2, 5)
    test_results = IntValidator(0, 100)

    def __init__(self, name: str, grades: tuple, test_results: tuple):
        self.test_results = test_results
        self.grades = grades
        self.name = name

    def average_score_on_tests(self):
        return int(sum(self.test_results) / len(self.test_results))

    def __str__(self):
        return f'{self.name}:\n\tGrades:\n\t\t{self.grades}\n\tTest results:\n\t\t{self.test_results}\n\n'


def get_subjects_from_csv(file_name) -> list:
    subjects = []
    with open(file_name, 'r', newline='', encoding='utf-8') as r_csv:
        reader = csv.reader(r_csv)

        for row1, row2, row3 in zip(reader, reader, reader):
            ins = Subject(row1[0].replace(' ', ''), tuple(map(int, row2)), tuple(map(int, row3)))
            subjects.append(ins)
    return subjects


def add_subject_to_csv(file_name, ins_subj):
    with open(file_name, 'a', newline='', encoding='utf-8') as a_csv:
        writer = csv.writer(a_csv)
        writer.writerow([])
        writer.writerows([[ins_subj.name]])
        writer.writerow(ins_subj.grades)
        writer.writerow(ins_subj.test_results)


if __name__ == '__main__':

    a = Subject('New', (4, 5), (45, 18))
    # add_subject_to_csv('my_file.csv', a)
    # abc = get_subjects_from_csv('my_file.csv')
    # print(*abc)

    print(a.average_score_on_tests())
