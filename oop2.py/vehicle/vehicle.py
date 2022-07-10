class Vehicle:
    def __init__(self,name,wheels,maxspeed) -> None:
        self.name = name
        self.wheels = wheels
        self._maxspeed = maxspeed
        self.__vin = None

    def set_vin(self,vin):
        self.__vin = vin

    def v_detail(self):
        print(f'================\nName : {self.name}\n================\nWheels : {self.wheels}\nmaxspeed : {self._maxspeed}\nVin : {self.__vin}')