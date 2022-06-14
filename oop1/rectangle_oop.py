from operator import length_hint


class Rectangle:
    def __init__(self,width,length) -> None:
        self.width = 0
        self.length = 0
        self.area = 0

    def get_data(self):
        self.width = float(input("Enter width: "))
        self.length = float(input("Enter length: "))

    def compute_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print(f"Reactangle Area :{self.area}")

#create object
rec_obj = Rectangle(4.5,8)
rec_obj.compute_area()
rec_obj.print_area()
