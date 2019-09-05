class Point:
    def __init__(self,x, y):  # This method is use to construct or create an object
        self.x = x
        self.y = y


    def move(self):
        print("move")


    def draw(self):
        print("draw")

point = Point(10, 20)
point.x = 11
point.y = 20
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, I am {}".format(self.name))


john = Person("John Smith")
john.talk()

bob = Person("Bob Rodrigez")
bob.talk()