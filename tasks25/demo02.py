class Switch:
    # Передается объект
    def info(sw_obj):
        if hasattr(sw_obj, 'hostname') and hasattr(sw_obj, 'model'):
            return 'Hostname: {}\nModel: {}'.format(sw_obj.hostname, sw_obj.model)
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
print(sw1.info())
print(sw2.info())
