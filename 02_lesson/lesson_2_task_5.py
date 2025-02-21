
# Напишите функцию month_to_season(), которая принимает один аргумент — номер месяца
# — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

def month_to_season(num_month):
    if  3 <= num_month <= 5:
        return "Весна"
    elif 6 <= num_month <= 8:
        return "Лето"
    elif 9 <= num_month <= 11:
        return "Осень"
    elif 2 <= num_month <= 12:
        return "Зима"
    else:
        print("Нет такого месяца")

try:
    num_month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(num_month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
