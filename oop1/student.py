from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH

class Student:
    def __init__(self,id:str,name:str,major:str = 'IT') -> None:
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Major : {self.major}')

    def __del__(self):
        print('Your information was deleted')

if __name__ == '__main__':
    jessica = Student('111','Jessica','IT')
    jessica.display_detail()
    print('----------------')

    john = Student('112','John','MKT')
    john.display_detail()
    print('----------------')

    john = Student('113','Amy')
    john.display_detail()
    print('----------------')