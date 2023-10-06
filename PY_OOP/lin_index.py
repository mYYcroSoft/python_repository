class linear: 
    def __init__(self, a = 1, b = 0):
        self.a = a 
        self.b = b
    
    def countlin(self):
        return -self.b/self.a

    def __str__(self):
        try:
            x = self.countlin()
        except:
            return "Chyba";
        else:
            return f"Linerání rovnice: {self.a} x {self.b} = {x}"
           

rovnice = linear(3,-13)

print(rovnice)         