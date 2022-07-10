from project import Project
class Condo(Project):
    def  __init__(self, name, time, location) -> None:
        super().__init__(name, time, location) 
        self.__budget #budget's instance variable
        self.type = 'Condo'

    def show(self):
        super().show()
        print(f'type : {self.type}')
        print(f'condo budget : {self.__budget} MB')
        print(f'project budget : {super().__budget} MB') 
