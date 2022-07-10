class Shape:
    def  __init__(self) -> None:
        self._shape = Shape
        self._area = 0

    @property
    def shape(self):
        return self._shape
    @shape.setter
    def shape(self,value):
        self._shape - value
    
    #area property
    @property
    def area(self):
        return self._area
    @area.setter
    def area(self,value):
        self._area = value
    
    def computer_area(self):
        pass