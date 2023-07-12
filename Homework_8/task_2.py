# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle


def read_csv_as_pickle(csv_file):
    with open(csv_file, 'r', encoding='utf8', newline='') as csv_rf:
        csv_file = csv.reader(csv_rf)
        pickle_list = []
        for line in csv_file:
            pickle_list.append(line)
        print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    read_csv_as_pickle('out/task_5_sem.csv')
