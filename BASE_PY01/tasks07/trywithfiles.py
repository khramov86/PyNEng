try:
    f = open('r3.txt', 'r')
    print(f.read())
except IOError:
    print('No such file')
finally:
    # не хватает обработки на тот случай, если файла не существует
    f.close()

