a = input('')
b = input('')
c = input('')
if type(a) == str and type(b) == str and type(c) == str:
    print('введено недопустимое значение')
else:
    x1 = 0
    x2 = 0
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        print(x1, x2)
    if D == 0:
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        print(x1)
    if D < 0:
        print('корней уравнения не существует')
