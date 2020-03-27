f = open('r1.txt', 'r')

test = f.read()
print(test)
print("Print without seeking")
#Ничего не выведется, т.к. файл не промотан назад
print(f.read())