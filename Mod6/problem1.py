'''
Create a list of integers (you get to pick!).
Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
'''
numbers = [1, 6, 3, 4, 5, 10, 22, 9]  #List of the integers
even_sum = 0                          #Initial counter
for num in numbers:                   #Loop through the integers list
    if num %2==0:
        even_sum += num
print("The sum of all even numbers is: ",even_sum)





