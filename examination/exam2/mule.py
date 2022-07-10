class Mule:
   
    mule_name = 'Mamu'

    def  __init__(self,color) -> None:
        self.color = color
        color = 'Color : Blue eyed cream'
        print (color)
        age = 'Age : 3'
        print (age)
        weight = 'Weight : 200kg'
        print (weight)
        
        run = 'Mule is running'
        print (run)
        
    def show(self):
        return f'{Mule.mule_name} has {self.color}'

if __name__ == '__main__':
    print(f'Name : Mamu')
    my_mule = Mule('************',)
    print(my_mule.show())

class Mule:
   
    mule_name = 'Meme'

    def  __init__(self,color) -> None:
        self.color = color
        color = 'Color : Polomino'
        print (color)
        age = 'Age : 1'
        print (age)
        weight = 'Weight : 120.7kg'
        print (weight)
        
    def show(self):
        return f'{Mule.mule_name} has {self.color}'

if __name__ == '__main__':
    print(f'Name : Meme')
    my_mule = Mule('************',)
    print(my_mule.show())