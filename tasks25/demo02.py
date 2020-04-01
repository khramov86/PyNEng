"""
    https://pyneng.readthedocs.io/ru/latest/book/25_oop_basics/create_methods.html
"""
class Switch:
    # Передается объект
    def info(self):
        if hasattr(self, 'hostname') and hasattr(self, 'model'):
            return 'Hostname: {}\nModel: {}'.format(self.hostname, self.model)
        else:
            return "Обязательные аттрибуты для объекта - hostname, model"


sw1 = Switch()
sw1.hostname = 'sw1'
sw1.model = 'Cisco 3850'
# print(sw1)
# Вернет адрес объекта
# <__main__.Switch object at 0x0102E628>
# можно назначить значения объекту класса
sw2 = Switch()
sw2.hostname = 'sw2'
#sw2.model = 'Cisco 3750'
# с self sw1.info() преобразуется в Switch.info(sw1)

'''Во втором случае, в параметре self уже больше смысла, он действительно принимает ссылку на экземпляр и на 
основании этого выводит информацию. 

С точки зрения использования объектов, удобней вызывать методы используя первый вариант синтаксиса, поэтому, 
практически всегда именно он и используется. '''
print(sw1.info())
print(sw2.info())

# Внутри стандратных методов происходит тоже самое
# a.append(5)
# по факту работает так
# list.append(a, 5)
