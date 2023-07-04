
class Animal:

    def __init__(self, breed, name):
        self.animalBreed = breed
        self.animalName = name
    
    def move(self):
        print(f"{self.animalName} moves.")
    
    def eat(self):
        print(f"{self.animalName} eat....")
    
    def breath(self):
        print(f"{self.animalName} breaths....")

class Dog(Animal):

    def __init__(self, breed, name):
        super().__init__(breed, name)
        self.dogBreed = breed
        self.dogName = name
    
    def bark(self):
        print("wooff....")
    
    def security(self):
        print(f"{self.dogName} is the security of the house.")

class Cat(Animal):

    def __init__(self, breed, name):
        super().__init__(breed, name)
        self.catBreed = breed
        self.catName = name
    
    def meaw(self):
        print("Meaww....")


myDog = Dog("Labrador", "Dama")
print(myDog.dogBreed)
print(myDog.dogName)
myDog.eat()

myCat = Cat("Siames", "Leo")
myCat.eat()
myCat.meaw()