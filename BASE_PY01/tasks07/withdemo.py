with open('r1.txt', 'r') as f:
    for line in f:
        # split to split every line to list, default delimiter is whitespace
        # print(line.split())

        # предыдущем выводе, между строками файла были лишние пустые строки, так как print добавляет ещё один перевод
        # строки. Чтобы избавиться от этого, можно использовать метод rstrip
        # print(line.rstrip())
        pass

with open('r1.txt', 'r') as f:
    print(f.read())
