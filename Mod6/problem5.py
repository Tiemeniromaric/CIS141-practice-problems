'''
Create a list of integers.
Use a loop to build a new list where each element is the square of the corresponding element in the original list.
Print the new list.
'''
numbers = [4, 7, 3, 8, 9, 5, 2, 1]     #Original list
numbers_square = []                    #Empty list to store the square
for number in numbers:                 #Loop through the original list
    numbers_square.append(number ** 2)
print(numbers_square)
