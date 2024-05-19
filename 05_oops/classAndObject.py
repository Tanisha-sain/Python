class Car:
    total_car = 0

    def __init__(self, userBrand, userModel):
        # __brand is private
        self.__brand = userBrand            
        self.__model = userModel
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    # Encapsulation
    def get_brand(self):
        return self.__brand + "!"

    # PolyMorphism
    def fuel_type(self):
        return "Petrol or Diesel"

    # Static methods
    @staticmethod
    def general_description():
        return "Cars are means of transport."

    @property
    def model(self):
        return self.__model

# Inheritance --->
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize

    # PolyMorphism
    def fuel_type(self):
        return "Electric Charge"





my_tesla = ElectricCar("Tesla","Model S","85kWh")
safari = Car("Tata","Safari")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(my_tesla.fuel_type())
print(safari.fuel_type())

#print(my_tesla.model)
print(my_tesla.full_name())

# print(my_tesla.brand)
print(my_tesla.get_brand())

my_car = Car("Toyota","Corolla")
#safari.model = "City"
print(safari.model)


print(Car.total_car)
# print(my_car)
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

print(Car.general_description())
# print(my_car.general_description())


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

tesla = ElectricCarTwo("Tesla","Model S")

print(tesla.battery_info())
print(tesla.engine_info())