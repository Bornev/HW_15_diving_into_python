"""
Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и
строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить
дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать,
сколько раз повторить строку в выводе.

"""

import argparse

def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(
        description='Скрипт принимает число и строку, а также обрабатывает опции для повторения строки и вывода дополнительной информации.'
    )
    parser.add_argument('number', type=int, help='Целое число для вывода в процессе.')
    parser.add_argument('text', type=str, help='Строка, которая будет обработана и выведена.')
    parser.add_argument('--verbose', action='store_true', help='Если установлено, выводит дополнительные сведения.')
    parser.add_argument('--repeat', type=int, default=2, help='Указывает, сколько раз повторить строку (по умолчанию 2).')

    # Парсинг аргументов
    args = parser.parse_args()

    # Проверка корректности значения для --repeat
    if args.repeat < 1:
        print('Ошибка: Опция --repeat должна быть положительным числом.')
        return

    # Вывод дополнительной информации, если опция verbose установлена
    if args.verbose:
        print(f'Выполняется вывод строки "{args.text}" {args.repeat} раз с числом {args.number}.')

    # Вывод строки, повторенной указанное количество раз
    repeated_text = " ".join([args.text] * args.repeat)
    print(f'Число: {args.number}, Строка: {repeated_text}')

if __name__ == '__main__':
    main()