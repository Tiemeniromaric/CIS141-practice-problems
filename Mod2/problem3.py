
'''
Create a program that prompts for the side lengths
of a triangle and computes the area using Heron's formula.
'''
import math  # This command is to import the math library
a = int (input ("What is the first side of your triangle?"))
b = int (input ("What is the second side of your triangle?"))
c = int (input ("What is the third side of your triangle?"))
s = 1/2*(a+b+c)
A = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area",A)
