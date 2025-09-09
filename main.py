from datetime import date

def days_until_new_year():
    today = date.today()
    new_year = date(today.year+ 1, 1, 1) if today.month == 12 and today.day == 31 else date(today.year, 12, 31)
    days_left = (new_year - today).days

    possible_words = { 1: 'день', 2: 'дня', 3: 'дня', 4: 'дня' }
    day_word = possible_words.get(days_left % 10, 'дней') if 11 <= days_left % 100 <= 14 else possible_words.get(days_left % 10, 'дней')

    print(f'До Нового года осталось {days_left} {day_word}')

days_until_new_year()