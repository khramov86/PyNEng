f = open('r1.txt', 'r')

test = f.read()
print(test)
print("Что будет если вывести файл без перемотки")
# Ничего не выведется, т.к. файл не промотан назад
print(f.read())
f.seek(0)
print("Тестирование чтение файла после перемотки")
print(f.read())

print("Снова промотаем файл")
f.seek(0)
print("прочитаем строчку")
print(f.readline())
print("прочитаем еще одну строчку")
print(f.readline())
