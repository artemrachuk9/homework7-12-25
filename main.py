from datetime import datetime

def get_days_from_today(date_str):
    user_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    today = datetime.today().date()
    delta = (today - user_date).days
    return delta
print(get_days_from_today('2023-10-01'))  # Example usage
print(get_days_from_today('2030-01-01'))  # Example usage
print(get_days_from_today("2021-10-09"))



import random

def get_numbers_ticket(min_value=1, max_value=49, quantity=6):
    """ Набір унікальних випадкових чисел для лотерей """
    current_numbers = set()
    while len(current_numbers) < quantity:
        number = random.randint(min_value, max_value)
        current_numbers.add(number)
    return list(current_numbers)

# Example usage:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)






