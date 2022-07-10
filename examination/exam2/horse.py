class Horse:
   
    horse_name = 'Khan Khan'

    def  __init__(self,color) -> None:
        self.color = color
        color = 'Color : Grey'
        print (color)
        run = 'Khan Khan is running'
        print (run)

    def show(self):
        return f'{Horse.horse_name} has {self.color}'

if __name__ == '__main__':
    print(f'Name : Khan Khan')
    my_horse = Horse('Max Height : 200cm')
    print(my_horse.show())
