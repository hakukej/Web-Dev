from models import Vehicle, Car, Motorcycle


def main():

    vehicle1 = Vehicle("Generic", "Transport", 2020)
    car1 = Car("Toyota", "Camry", 2022, 4)
    moto1 = Motorcycle("Yamaha", "R1", 2021, 1000)

    vehicles = [vehicle1, car1, moto1]

    for v in vehicles:
        print(v)              # __str__
        print(v.start_engine())
        print(v.move())       # polymorphism
        print(v.stop_engine())
        print()


if __name__ == "__main__":
    main()