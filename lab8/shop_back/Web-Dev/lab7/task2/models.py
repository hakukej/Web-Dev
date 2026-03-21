class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model} engine started."

    def stop_engine(self):
        return f"{self.brand} {self.model} engine stopped."

    def move(self):
        return f"{self.brand} {self.model} is moving."

    def __str__(self):
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self):   # method overriding
        return f"Car {self.brand} {self.model} drives on the road."

    def open_trunk(self):
        return f"{self.brand} {self.model}'s trunk is open."

    def __str__(self):
        return f"Car: {self.brand} {self.model}, {self.year}, Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def move(self):   # method overriding
        return f"Motorcycle {self.brand} {self.model} speeds on the road."

    def wheelie(self):
        return f"{self.brand} {self.model} performs a wheelie!"

    def __str__(self):
        return f"Motorcycle: {self.brand} {self.model}, {self.year}, Engine: {self.engine_capacity}cc"