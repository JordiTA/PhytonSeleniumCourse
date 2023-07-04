"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""

import pdb

class Calculator:
    
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def Add(self):
        sum = self.number1 + self.number2
        return sum
    
    def Substract(self):
        substract = self.number1 - self.number2
        return substract
    
    def Multiply(self):
        product = self.number1 * self.number2
        return product
    
    def Divide(self):
        division = self.number1 / self.number2
        return division

calc = Calculator(6,3)

sum = calc.Add()
print(sum)

substract = calc.Substract()
print(substract)

product = calc.Multiply()
print(product)

division = calc.Divide()
print(division)