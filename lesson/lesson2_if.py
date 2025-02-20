# Ветвления

age = 18
if age < 17:
    print("Пейте сок!")

else:
    print("Можно не сок")

age = 20
print(age<18) # False True

if age<18:
    print("берем в школу")

if age>18:
    print("не берем в школу")


login = "elena"
password = "Qwerty12"

if (login == "elena") and (password == "Qwerty12"):
    print("Авторизация")
else:
    print("Неверный логин или пароль")


rate_as_str = input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_str)
if rate < 1:
    rate = 1

if rate > 5:
    rate = 5

feedback =""
if rate == 1:
    feedback=input("Расскажи, что не так:")
else:
    if rate == 2:
        feedback = input("Почему такая оценка:")
    else:
        if rate == 3:
            feedback = input("Что улучшить:")
        else:
            if rate == 4:
                feedback = input("Расскажи, почему не 5")
            else:
                if rate == 5:
                    feedback = input("Спасибо огромное")