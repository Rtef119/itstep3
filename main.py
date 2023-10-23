class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passengers in args:
            self.passengers.append(passengers)


    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Імена пасажирів в авто:{self.brand}")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"В авто {self.brand} пасажири відсутні")

car = Auto("Ваз 2101")
for i in range(4):
    p1 = Human(input("Ведіть ім'я пасажира:"))
    car.add_passengers(p1)

car.print_passengers_names()