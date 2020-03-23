# ZeroDivisionError: division by zero
# print(2/0)
# TypeError: can only concatenate str (not "int") to str
# print('test' + 2)
# try:
#     2 / 0
#
# except:
#     print("You can't divide by zero")
#

try:
    print("Let's divide some numbers")
    #Всё выполниться до этого выражения
    2/0
    print("Cool!")
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Неверное значение")
finally:
    print("Выполняется всегда")

