import requests
from bs4 import BeautifulSoup


def write_to_file(line):
    with open('../TODO.md', 'a', encoding='utf8') as f:
        f.write(line)


header = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
base_url = 'https://pyneng.readthedocs.io/ru/latest/'

with requests.Session() as s:
    r = s.get(base_url, headers=header)
    # print(r.text)
    # r.content в байтах vs r.text в строках
    soap = BeautifulSoup(r.content.decode('utf8'), 'html.parser')
    # print(soap)

    lst = []
    dct = {}
    for line in soap.find_all('a', class_='reference internal'):

        if line.contents[0] in dct.keys():
            continue
        else:
            # lst.append(line.contents[0])
            dct[line.contents[0]] = line.get('href')

        # print(x)
        # y = range(10)
        # print(y)
        # lst = [s for s in range(10)]
    romenums = 'IVX'
    lst = ''
    for key, value in dct.items():
        par_url = base_url + value
        # for tmp in dct.keys():
        # print(tmp)

        for a in romenums:

            if key.startswith(a):
                lst += f'{key} ссылка {base_url + value}\n'
                # print(lst)
                # print(f'- [ ] {key} ссылка ({base_url + value})'.encode('utf8').decode('utf8'))
                # write_to_file(f'- [ ] {key} \n\n{base_url+value}\n')
    # print(lst)
    dct = {}
    lst = lst.strip().split('\n')
    for l in lst:
        temp = l.split('ссылка')

        dct[temp[0].strip()] = temp[1].strip()
    # print(dct)

    for key, value in dct.items():
        write_to_file(('- [ ] {} {}\n'.format(key, value)))

        pars = BeautifulSoup(s.get(value, headers=header).content.decode('utf8'), 'html.parser').find_all('li',
                                                                                                          class_='toctree-l1')
        for par in pars:
            if par.get_text()[0].isdigit():
                write_to_file('\n\t- [ ] {}\n'.format(par.get_text()[3:].strip()))
        write_to_file('\n')
#

#     print(par.get_text())
