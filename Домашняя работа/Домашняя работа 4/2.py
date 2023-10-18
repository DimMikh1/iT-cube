a = int(input())

if a == 0:
    print("Зеленый")
elif a >= 1 and a <= 10 or a >= 19 and a <= 28:
    if a % 2 != 0:
        print("Красный")
    else:
        print("Черный")
elif a >= 11 and a <= 18 or a >= 29 and a <= 36:
    if a % 2 != 0:
        print("Черный")
    else:
        print("Красный")
else:
    print("Ошибка ввода")