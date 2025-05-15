'''
Create a list of integers (you get to pick!).
Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
'''
#List of the integers
numbers = [1, 6, 3, 4, 5, 10, 22, 9]

#Initial counter
even_sum = 0

#Loop through the integers list
for num in numbers:
    if num %2==0:
        even_sum += num

#Print the result (sum of all even numbers)
print("The sum of all even numbers is: ",even_sum)


