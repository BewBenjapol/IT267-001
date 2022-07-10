from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, name, wheels, maxspeed) -> None:
        super().__init__(name, wheels, maxspeed)
        self.cc = None

    def set_cc(self,cc):
        self.cc = cc

    def bike_detail(self):
        print(f'cc : {self.cc}')