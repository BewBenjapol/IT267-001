class Person:
    def __init__(self,name,gender,profession,study) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study2 = study

    def work(self):
        print(f'{self.name} is working as a {self.profession}')

    def study(self):
        print(f'{self.name} studies for {self.study2} hours')

    def show(self):
        print(f'Name : {self.name} Gender : {self.gender} Profession : {self.profession} Study {self.study2,} hours')

rec_obj = Person('Jessa','Male','Software Engineer',10)
rec_obj.work()
rec_obj.study()
rec_obj.show()
rec_obj = Person('John','Male','Profession',15)
rec_obj.show
rec_obj.work()
rec_obj.study()

rec_obj = Person('Lisa','Female','Korean Singer',15)
rec_obj.work()
print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')

