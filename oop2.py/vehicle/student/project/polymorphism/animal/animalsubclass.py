from animal import Animal

class Dog(Animal):
    def info(self):
        #super().info()
        Animal.info(self) #---Animal
        print('I am a dog.')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')
        
    def make_sound(self):
        Animal.make_sound(self)##==== Animal Sound ====
        print(f'Hey I male Woof!! Woof!! sound.')

class Cow(Animal):
    def info(self):
        #super().info()
        Animal.info(self) #---Animal
        print('I am a cow.')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')
    
    def make_sound(self):
        Animal.make_sound(self)##==== Animal Sound ====
        print(f'Hey I male Moo!! Moo!! sound.')


