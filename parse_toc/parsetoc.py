import requests
from bs4 import BeautifulSoup
def write_to_file(line):
    with open('../TODO.md', 'a') as f:
        f.write(line.encode('utf8').decode('utf8'))

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
    for key,value in dct.items():


    #for tmp in dct.keys():
        #print(tmp)
        for a in romenums:
            if key.startswith(a):
                print(f'- [ ] {key} ссылка ({base_url+value})'.encode('utf8').decode('utf8'))
                write_to_file(f'- [ ] {key} \n\n{base_url+value}\n')


#
                # for par in BeautifulSoup(s.get(url_of_cont, headers=header).content.decode('utf8'), 'html.parser').find_all('a', class_='reference internal'):
                #     print(par.get_text())

