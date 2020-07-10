import yaml
from pprint import pprint

with open('test.yml') as f:
    templates = yaml.safe_load(f)

def dict_unpack(tempdict):
    for key,value in tempdict.items():
        if type(value) is dict:
            dict_unpack(value)
        else:
            if type(value) is list and type(word) in value is dict:
                dict_unpack(word)
            else:
                print(key, value)

for word in templates:

    if type(word) is dict:
        dict_unpack(word)
    else:
        print(word)
