class Mobile:
    def __init__(self, wheels=0):
        self.wheels = wheels

    def __str__(self):

        return str(self.wheels)

    def GasCalc(self):

        return 10/2

class Car(Mobile):
    def __init__(self):
        super().__init__(wheels=4)
    def __str__(self):

        return "The Car has " + str(self.wheels) + "!"

class Moto(Mobile):
    def __init__(self):
        super().__init__(wheels=2)

    def GasCalc(self):
        return super().GasCalc()/2


#mobile = Mobile()
mobile = Car()
mobile2 = Moto()

print(mobile.GasCalc())
print(mobile2.GasCalc())
# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
