"""
Write a program that takes an integer input and checks if it's even number.
Prints out 'True' if the number is even and 'False' if the number is not even.

e.g.
Input: 2
Output: 2 is even

Input: 3
Output: 3 is not even
"""

print("WE ARE GOING TO FIGURE OUT EVEN OR NOT EVEN NUMBERS!")

number = int(input("Type the number you want to check: "))

if number % 2 == 0:
    print("This number is EVEN")
else:
    print("This number is NOT EVEN")