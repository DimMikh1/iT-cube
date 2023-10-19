a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a % 2 == c % 2 and b % 2 == d % 2:
    print("Да")
elif a % 2 != c % 2 and b % 2 != d % 2:
    print("Да")
else:
    print("Нет")