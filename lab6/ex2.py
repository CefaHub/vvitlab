class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Транспорт: {self.make} | Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Транспорт: {self.make} | Модель: {self.model} | Топливо: {self.fuel_type}"

print('\nИнформация:')
v1 = Vehicle("Yamaha", "R1")
c1 = Car("Lotus", "Emira", "Бензин")
c2 = Car("Tesla", "Model 3", "Электричество")

print(v1.get_info())
print(c1.get_info())
print(c2.get_info())
