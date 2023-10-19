a = int(input())

if a % 2 == 1:
    print("Да")
elif a % 2 == 0 and 2 <= a <= 5:
    print("Нет")
elif a % 2 == 0 and 6 <= a <= 20:
    print("Да")
elif a % 2 == 0 and a > 20:
    print("Нет")