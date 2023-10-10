

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
