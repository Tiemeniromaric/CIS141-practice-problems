'''
Create a list of integers.
Write code that counts how many numbers are positive and how many are negative, then print both counts.
'''
whole_numbers = [1, 3, -2, 7, -8, -6, 5, 2, -3, 0]    #create the list of intergers
positive_count = 0
negative_count = 0             #Initiale counters
for number in whole_numbers:   # loop through the list
    if number >=0:
        positive_count += 1
    else:
        negative_count +=1
print("we have:",positive_count,"Positive numbers,","and",negative_count, "Negative numbers.")
print("We have:",positive_count+negative_count,"whole numbers.")
