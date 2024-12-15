"""
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.

"""

import logging

# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Форматтер для сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для сообщений уровня DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)

# Фильтр для DEBUG и INFO
class DebugInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.INFO)

debug_info_handler.addFilter(DebugInfoFilter())
logger.addHandler(debug_info_handler)

# Обработчик для сообщений уровня WARNING и выше
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)

# Фильтр для WARNING и выше
class WarningsErrorsFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING

warnings_errors_handler.addFilter(WarningsErrorsFilter())
logger.addHandler(warnings_errors_handler)

# Логирование сообщений различных уровней
logger.debug('Это сообщение уровня DEBUG.')
logger.info('Это сообщение уровня INFO.')
logger.warning('Это сообщение уровня WARNING.')
logger.error('Это сообщение уровня ERROR.')
logger.critical('Это сообщение уровня CRITICAL.')

# Закрытие обработчиков
for handler in logger.handlers:
    handler.close()
    logger.removeHandler(handler)