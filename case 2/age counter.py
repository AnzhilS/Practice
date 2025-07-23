import datetime

#Запрос дня рождения у пользователя
while True:
    user_day = int(input("Введите день вашего рождения: "))
    user_month = int(input("Введите месяц вашего рождения: "))
    user_year = int(input("Введите год вашего рождения: "))
    print(f"Ваша дата рождения {user_day} {user_month} {user_year} Верно? Да/Нет")
    mistake = input("Ваш ответ: ")
    if mistake == 'Нет':
        continue

#Подсчет возраста
    TODAY = datetime.date.today()
    print(f'Вам {TODAY.year - user_year - ((TODAY.month, TODAY.day) < (user_month, user_day))} лет!')

#Какому дню недели соответствует день рождения
    week_days = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    week_num = datetime.date(user_year, user_month, user_day).weekday()
    print(f'Вы родились в {week_days[week_num]}!')

#Високосный год
    if user_year % 4 == 0:
        print('Вы родились в високосный год.')
    elif user_year % 100 == 0:
        print('Вы родились в не високосный год.')
    elif user_year % 400 == 0:
        print('Вы родились в високосный год.')
    else:
        print('Вы родились в не високосный год.')
