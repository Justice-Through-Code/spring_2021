from inheritance import Bird, Penguin

class Parrot(Bird):

    def __init__(self):
        super().__init__()
        self.__food_store = 6

    def fly(self):
        print("Parrot can fly")

# common interface
def flying_test(bird):
    bird.fly()

polly = Parrot()
mumble = Penguin()

flying_test(polly)
flying_test(mumble)

#       bird
# /          \
#penguin    parrot