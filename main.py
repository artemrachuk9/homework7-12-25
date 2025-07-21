from datetime import datetime

def get_days_from_today(date_str):

    try:
        user_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = (today - user_date).days
        return delta
    except ValueError:
        return " Неправильний формат дати. Використовуйте YYYY-MM-DD"
print(get_days_from_today("2023-02-10"))  # Інший формат
print(get_days_from_today("13.14.2000"))  # Некоректна дата
print(get_days_from_today("2020/12/01"))  # Правильний формат 





import random

def get_numbers_ticket(min_value=1, max_value=49, quantity=6):
    """
    Генерує унікальний набір випадкових чисел для лотереї.
    Якщо параметри некоректні або числа надто великі — повертає [].
    """
    MAX_ALLOWED = 49
    MIN_ALLOWED = 1
    if (
        min_value > max_value or
        quantity < 1 or
        quantity > (max_value - min_value + 1) or
        min_value < MIN_ALLOWED or
        max_value > MAX_ALLOWED
    ):
        return []
    current_numbers = set()
    while len(current_numbers) < quantity:
        current_numbers.add(random.randint(min_value, max_value))
    return sorted(current_numbers)
print(get_numbers_ticket(-10, 10, 5))    # ➡ []
print(get_numbers_ticket(1000, 1200, 10)) # ➡ []
print(get_numbers_ticket(10, 4, 5))       # ➡ []
print(get_numbers_ticket(10, 14, 6))      # ➡ []
print(get_numbers_ticket(1, 49, 6))       # ➡ [коректний список]





