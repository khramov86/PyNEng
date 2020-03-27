with open('r1.txt', 'r') as src, open('result.txt', 'r+') as dest:
    for line in src:
        if line.startswith('service'):
            # print(line)
            dest.write(line)
    dest.seek(0)
    print(dest.read())
