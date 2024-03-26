class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal): #Allows Fish class to inherit everything from the superior class (Animal)
    def __init__(self):
        super().__init__()
    
    def breathe(self): # we can inherit a attribute from the super class and add to it by ...
        super().breathe # ... calling the attribute from the super class in a new funct. and adding any ammendments on the end
        print("doing this underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)