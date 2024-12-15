"""
Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование.

"""

import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

# Определение namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

# Настройка логирования
logging.basicConfig(
    filename='directory_contents.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def collect_info(directory_path):
    """
    Собирает информацию о содержимом директории и сохраняет в лог.
    :param directory_path: Путь до анализируемой директории.
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не является директорией.")

    parent_directory = os.path.basename(os.path.abspath(directory_path))

    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_dir():
                file_info = FileInfo(name=entry.name, extension=None, is_directory=True, parent_directory=parent_directory)
            else:
                name, extension = os.path.splitext(entry.name)
                file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)

            # Запись в лог
            logging.info(
                f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | '
                f'{"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}'
            )

            # Опционально, вывод в консоль
            print(f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | '
                  f'{"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}')


def main():
    """
    Основная функция для обработки командной строки и сбора информации.
    """
    parser = ArgumentParser(description="Сбор информации о содержимом директории и запись в лог.")
    parser.add_argument('directory', type=str, help="Путь до директории для анализа")
    args = parser.parse_args()

    try:
        collect_info(args.directory)
        print(f'Информация о содержимом директории "{args.directory}" успешно записана в файл "directory_contents.log".')
    except ValueError as e:
        print(f'Ошибка: {e}')
    except PermissionError:
        print('Ошибка: Недостаточно прав для доступа к указанной директории.')
    except FileNotFoundError:
        print('Ошибка: Указанная директория не найдена.')
    except Exception as e:
        print(f'Непредвиденная ошибка: {e}')


if __name__ == '__main__':
    main()
