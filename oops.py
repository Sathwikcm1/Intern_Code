class Car: 
    def __init__(self,color,wheels):
        self.color = color
        self.wheels = wheels
        print('wheels')

    def brake(self):
        print('stopped')

car1 = Car("read",4)
