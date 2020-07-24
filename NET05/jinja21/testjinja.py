from jinja2 import Template


def loadfile():
    with open('test.j2', 'r') as f:
        template = f.read()
        return template


liverpool = {'id': '11', 'name': 'Liverpool', 'int': 'Gi1/0/17', 'ip': '10.1.1.10'}

template = Template(loadfile())
print(template.render(liverpool))
