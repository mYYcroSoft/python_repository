
class Computer:
    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__ram = kwargs['ram']
        self.__cpu = kwargs['cpu']

class Monitor:
    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__display = kwargs['display']
        self.__resolution = kwargs['resolution']

class Keyboard:
    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__type = kwargs['type']
        self.__color = kwargs['color']

class Mouse:
    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__type = kwargs['type']
        self.__color = kwargs['color']


produkty = ['Computer', 'Monitor', 'Keyboard', 'Mouse']
class ElectronicFactory:
    def __init__(self, name):
        self.__name = name    


    @staticmethod
    def produce(**kwargs):
        if kwargs['type'] in produkty:
            return  globals()[kwargs['type']](**kwargs)
        else:
            return None 


storage = []

storage.append(ElectronicFactory.produce(type = 'Computer', name ="Asus Tuf", ram = "16GB", cpu = "Intel i5"))


print(storage)

for x in storage:
    print(x)
