import random

class brake:
    def __init__(self, first_brake_quality):
        self.__first_brake_quality = first_brake_quality
        self.generate_max_brake()
    def generate_max_brake(self):
         self.brake_quality = random.randint(1, self.__first_brake_quality + 1)
    def getBrake(self):
        return self.brake_quality

class EngineSpeed:
    def __init__(self, first_max_speed):
        self.__first_max_speed = first_max_speed
        self.generate_max_speed()
    def generate_max_speed(self):
         speed_quant = self.__first_max_speed / 2
         self.max_speed = random.randint(speed_quant + (random.randint(0,6)) - random.randint(0,3) , speed_quant * random.randint(2,4) - random.randint(0,7))
    def getEnginespeed(self):
        return self.max_speed
    

class enemy:
    def __init__(self, vehicle_name, first_max_speed, first_brake_quality):
        self.__first_max_speed = first_max_speed
        self.__first_brake_quality = first_brake_quality
        self.__vehicle_name = vehicle_name
         # ---------------------------------------------------------------------------------------
        self.Brakes =  brake(self.__first_max_speed)
        self.Engine = EngineSpeed(self.__first_max_speed)

    def getEnemyData(self):
        return {"Name": self.__vehicle_name, "Engine": self.Engine.getEnginespeed(), "Brake": self.Brakes.getBrake()}
    
    
    def __str__(self):
     
        return f"Vozidlo soupeře: {self.__vehicle_name} má maximální rychlost {self.Engine.getEnginespeed()} a kvalitu brzd {self.Brakes.getBrake()}"
    pass

class vehicle:
    def __init__(self, vehicle_name, max_speed, brake_quality):
        self.__vehicle_name = vehicle_name
        self.__default_max_speed = max_speed
        self.__default_max_brake_quality = brake_quality
        # ---------------------------------------------------------------------------------------
        self.Engine = EngineSpeed(self.__default_max_speed)
        self.Brakes = brake(self.__default_max_brake_quality)        
        self.enemy = enemy("Skoda", self.__default_max_speed, self.__default_max_brake_quality) 

    def GetEnemy(self):
        enemy = self.enemy.getEnemyData()
        return f"Vozidlo soupeře {enemy['Name']} má maximální rychlost {enemy['Engine']} a kvalitu brzd  {enemy['Brake']}"
    
    def getEnemyData(self):
        return self.enemy.getEnemyData()
    
    def vehicleData(self):
        return {"Name": self.__vehicle_name, "Engine": self.Engine.getEnginespeed(), "Brake": self.Brakes.getBrake()} 
        
    def __str__(self):
        return  f"Tvoje vozidlo: {self.__vehicle_name} má maximální rychlost {self.Engine.getEnginespeed()} a kvalitu brzd {self.Brakes.getBrake()}" 
        
    
    pass





#car_enemy = enemy('Škodovka', 20, 2)
#print(car_enemy)

vehicle_name = str(input("Název vozidla: "))
max_speed = int(input("(max 40) Maximální rychlost: "))
max_brake = int(input("(max 40) Maximální kvalita brzd: "))


vehicles = vehicle("Škoda", 20, 2)
print("__________________________________________")
print(vehicles)
print(vehicles.GetEnemy())
print("__________________________________________")

