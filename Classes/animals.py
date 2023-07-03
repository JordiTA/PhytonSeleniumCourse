import pdb

class Animal:
    
    def __init__(self, color, foodType):
        print("Init Animal.")
        self.color = color
        self.foodType = foodType

    def move(self):
        print("Animal moves.")
    
    def eat(self):
        print("Animal eat.")
        print(f"This animal eats {self.foodType}.")

    def breath(self):
        print("Animal breath.")

    def main(self):
        self.move()
        self.eat()
        self.breath()

print('-------------------------------------') # Separator

animal1 = Animal('blue', 'meat')
print(f"Color of animal 1: {animal1.color}.")
print(f"Food type of animal 1: {animal1.foodType}.")
animal1.main()

print('-------------------------------------') # Separator

animal2 = Animal('red', 'veg')
print(f"Color of animal 2: {animal2.color}.")
print(f"Food type of animal 2: {animal2.foodType}.")
animal2.main()

print('-------------------------------------') # Separator

# pdb.set_trace()