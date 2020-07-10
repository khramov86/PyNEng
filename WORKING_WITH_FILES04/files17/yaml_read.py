import yaml
from pprint import pprint

with open('info.yml') as f:
    templates = yaml.safe_load(f)


for item in templates:
    for key,value in item.items():
        print(key,value)