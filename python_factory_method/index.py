

class computer:
    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__ram = kwargs['ram']
        self.__cpu = kwargs['cpu']




class ElectronicFactory:
    produkty = ['Computer', 'Monitor', 'Keyboard', 'Mouse']
    def __init__(self, name):
        self.__name = name    


    @staticmethod
    def produce(**kwargs):
        if kwargs['type'] == ElectronicFactory.produkty:
            return globals()[kwargs['type']](**kwargs)
        else:
            return None 


storage = []

storage.append(ElectronicFactory.produce(type = 'Computer'), name ="Asus Tuf", ram = "16GB", cpu = "Intel i5")


for x in storage:
    print(x)
