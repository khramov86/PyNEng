# -*- coding: utf-8 -*-

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")