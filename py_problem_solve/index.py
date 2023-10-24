import random

class enemy:
    def __init__(self, first_vehicle_name, first_max_speed, first_brake_quality):
        self.__first_vehicle_name = first_vehicle_name
        self.__first_max_speed = first_max_speed
        self.__first_brake_quality = first_brake_quality
        self.generate_enemy()

    def generate_enemy(self):
        self.__vehicle_name = "Tojotinka"  
        self.__max_speed = self.generate_max_speed()
        self.__brake_quality = self.generate_brake_quality()

    def generate_max_speed(self):
         speed_quant = self.__first_max_speed / 2
         max_speed = random.randint(speed_quant + (random.randint(0,6)) - random.randint(0,3) , speed_quant * random.randint(2,4) - random.randint(0,7))
         return max_speed

    def generate_brake_quality(self):
        brake_quality = random.randint(1, self.__first_brake_quality + 1)
        return brake_quality

    def __str__(self):
        print(f"Soupořovo vozidlo {self.__vehicle_name} má maximální rychlost {self.__max_speed} a kvalitu brzd {self.__brake_quality}")
    pass

class vehicle:
    def __init__(self, vehicle_name, max_speed, brake_quality):
        self.__vehicle_name = vehicle_name
        self.__max_speed = max_speed
        self.__brake_quality = brake_quality

    pass



car_enemy = enemy('Škodovka', 20, 2)

print(car_enemy)



