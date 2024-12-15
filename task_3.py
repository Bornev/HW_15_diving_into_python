"""
Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.

"""

from datetime import datetime, timedelta

def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
    Если количество дней отрицательное, возвращается дата в прошлом.
    
    :param days_from_now: Количество дней от текущей даты (может быть отрицательным).
    :return: Отформатированная дата в формате YYYY-MM-DD.
    
    Примеры:
    >>> future_date(30)
    '2024-09-08'
    >>> future_date(-10)
    '2024-07-30'
    """
    try:
        days_from_now = int(days_from_now)
    except ValueError:
        raise ValueError("Argument must be an integer representing the number of days.")
    
    today = datetime.now()
    future_date = today + timedelta(days=days_from_now)
    return future_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    try:
        days = int(input('Enter the number of days from now (can be negative): '))
        print(f'Date {days} days from now: {future_date(days)}')
    except ValueError:
        print("Please enter a valid integer.")