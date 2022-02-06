#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import click


@click.group()
def cli():
    pass


# Создаёт словарь "студент" и записывает его в файл
@cli.command()
@click.argument("file_name")
@click.option("-n", "--name")
@click.option("-g", "--group")
@click.option("-av", "--average_estimation")
def add(file_name, name, group, average_estimation):

    if os.path.exists(file_name):
        students = load_students(file_name)
    else:
        students = []

    # Создать словарь.
    student = {
        'name': name,
        'group': group,
        'average_estimation': average_estimation,
    }
    students.append(student)

    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(students, fout, ensure_ascii=False, indent=3)


# Выводит список студентов
@cli.command()
@click.argument("file_name")
def list(file_name):

    with open(file_name, "r", encoding="utf-8") as fin:
        staff = json.load(fin)

    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Ф.И.О.",
                "Группа",
                "Средняя оценка"
            )
        )
        print(line)

        # Вывести данные о всех студентах.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    student.get('average_estimation', 0)
                )
            )

        print(line)

    else:
        print("Список пуст")


# Выводит справку о работе с программой
@cli.command()
def help():

    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


# Читает данные из файла
def load_students(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        file = json.load(fin)
        return file


def main():
    cli()


if __name__ == '__main__':
    main()
