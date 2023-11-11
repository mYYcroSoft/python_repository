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
        self.generate_enemy()

    def generate_enemy(self):
        self.Engine =  brake(self.__first_max_speed)
        self.Brakes = EngineSpeed(self.__first_max_speed)

    def __str__(self):
        engine = self.Engine
        return f"Vozidlo soupeře: {self.__vehicle_name} má maximální rychlost {engine.getEnginespeed()} a kvalitu brzd {self.__brakes.getBrake()}"
    pass

class vehicle:
    def __init__(self, vehicle_name, max_speed, brake_quality):
        self.__vehicle_name = vehicle_name
        self.__max_speed = max_speed
        self.__brake_quality = brake_quality

    pass



car_enemy = enemy('Škodovka', 20, 2)

print(car_enemy)



