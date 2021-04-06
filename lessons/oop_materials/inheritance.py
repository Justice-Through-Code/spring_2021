# parent class
class Bird:
    # encapsulation example (self.__food_store)
    def __init__(self):
        print("New bird")

    def whoisThis(self):
        print("Bird")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("New penguin")

    # overriding
    def whoisThis(self):
        print("Penguin")

    def fly(self):
        print("Penguin is flying")

peggy = Penguin()
peggy.whoisThis()
# peggy.fly()