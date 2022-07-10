class Donkey:
   
    donkey_age = 'Age : 2 year old'

    def  __init__(self,weight) -> None:
        self.weight = weight
        weight = 'Weight : 100kg'
        print (weight)
        run = 'Sound : Donkey Makes eeyore sound'
        print (run)
        
    def show(self):
        return f'{Donkey.donkey_age} has {self.weight}'

if __name__ == '__main__':
    print(f'Age : 2 year old')
    my_donkey = Donkey('Weight : 100kg')
    print(my_donkey.show())