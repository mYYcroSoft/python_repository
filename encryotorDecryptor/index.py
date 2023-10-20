
"""
class rail:
    def __init__(self, string_world = 0):
        self.stringWorlds = string_world
    pass


class crypth:
    pass



class encrypt:
    string = ''
    number_of_rails = 0
    string_worlds = 0
    rails = []
    def __init__(self, string = 0, number_of_rails = 3): 
        self.string = string.replace(" ", "")
        self.number_of_rails = number_of_rails
        self.string_worlds = len(self.string)

    def genereateRailsArray(self):
        rails = []
        for i in range(self.number_of_rails):
            rails.append([rail(self.string_worlds)])
        return rails

    def __str__(self):
        return f"String: {self.string}    Počet kolejnic: {self.number_of_rails}    Počet slov: {self.string_worlds}"

    def writeRail(self):
        listString = list(self.string)
        for x in range(self.string_worlds):
            pass            
            





string = "Ahoj jak se máš?"
encrypt = encrypt(string)
encrypt.genereateRailsArray()

print(encrypt.writeRail())

"""


class encryptRail:
    string = ''
    number_of_rails = 0
    rails = []
    final_string = ''
    math = [0, 1, 2, 1, 0, 1, 2, 1, 0,1,2, 1, 2, 0, 1,2]
    
    def __init__(self, string , number_of_rails = 3):
         self.__string = string.replace(" ", "")    
         self.__number_of_rails = number_of_rails
         self.rails = [[] for _ in range(self.__number_of_rails)]
         
    def encrypt(self):
        string_list = list(self.__string)
        for x in range(len(self.__string)):
            rail_index = self.math[x]
            self.rails[rail_index].append(string_list[x])
        
        for rail in self.rails:
            for letter in rail:
                self.final_string += letter

        return self.final_string
        
    def __str__(self):
        return f'Původní string: {self.__string} O 3 kolejnicích s výstupem: {self.final_string}'


string = "TONAHRVOTAIOIT"

encrypt_text = encryptRail(string)
encrypt_text.encrypt()
print(encrypt_text)



    

    
