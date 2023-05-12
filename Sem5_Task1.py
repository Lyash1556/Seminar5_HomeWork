# **Задача 26:**  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N **ЧЕРЕЗ РЕКУРСИЮ**


def factor(n):
    if n == 1:
        return 1
    return factor(n - 1) * n

num = int(input('Enter number: '))

print(factor(num))