class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        
    def moves(self):      # Override method what ever it would inherit from Vehicle class.
        print("moves along")
        
    def get_details(self):
        print(f"I have a {self.name} {self.model} year is {self.year}.")
        
my_car = Vehicle("Bugatti", "chiron", "2021")
my_car.get_details()

my_car = Vehicle("Lamborghini", "Avtr", "2020")
my_car.get_details()


class Airplane(Vehicle):
    def __init__(self, name, model, year, JetLicense): # identical method
        super().__init__(name, model, year)    # inherit from the parent class.
        self.JetLicense = JetLicense
    def moves(self):
            print("Flies along")

class Truck(Vehicle):
    def moves(self):      # Override method what ever it would inherit from Vehicle class.
        print("Rumbles along")

class F1(Vehicle):      # inherit every thing ass it is
        pass 

airbus = Airplane("GulfStream","Bombardier", 2023, "GSB07776DV")
volvo = Truck("volvo","big-z", 2024)
mercedes = F1("benz","f1v8", 2025)


airbus.get_details()
airbus.moves()

volvo.get_details()
volvo.moves()

mercedes.get_details()
mercedes.moves()


print('\n\n')

for v in (my_car, airbus, volvo, mercedes): # (Plymorphisum) Ability to behave differently in response to same input messages.
    
    v.get_details()
    v.moves()

