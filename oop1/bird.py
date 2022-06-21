#global variable
bird_type = 'parrot'

class Bird:
    #class variable
    bird_name = 'peter'

    def  __init__(self,color) -> None:
    #instance variable
        self.color = color

    #local variable
        country = 'Thailand'
        print (country)

    def show(self):
        return f'{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'*********')
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())
