a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a - c) ** 2 == (b - d) ** 2 or (a == c) ** 2 or (b == d) ** 2:
    print("Да")
else:
    print("Нет")