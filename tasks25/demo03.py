"""Параметр self указывался выше в определении методов, а также при использовании переменных экземпляра в методе.
Параметр self это ссылка на конкретный экземпляр класса. При этом, само имя self не является особенным,
а лишь договоренностью. Вместо self можно использовать другое имя, но так делать не стоит.
 """


class Switch:
    '''
    Метод __init__ иногда называют конструктором класса, хотя технически в Python сначала выполняется метод __new__,
    а затем __init__. В большинстве случаев, метод __new__ использовать не нужно.
    '''

    def __init__(self, hostname, model):
        self.hostname = hostname
        self.model = model
    def generate_interfaces (self, intf_type, number_of_intf):
        interfaces = ['{}{}'.format(intf_type, number) for number in range(1, number_of_intf+1)]
        self.interfaces = interfaces
    # Так делать не стоит, принято принимать объект через self
    def info(sw_object):
        print('Hostname: {}\nModel: {}'.format(sw_object.hostname, sw_object.model))


# sw1 = Switch()
# print(sw1)
#
# sw1.hostname = 'mySwitch'
# sw1.model = 'myModel'
# sw1.generate_interfaces('Fa', 10)
# print(sw1.interfaces)

sw2 = Switch('myModel', 'mySwitch')
print(sw2.hostname, sw2.model)

# Switch.info(sw1)
