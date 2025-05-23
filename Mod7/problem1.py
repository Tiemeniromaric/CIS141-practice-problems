'''
Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''
# First way to sole the problem
def count_vowels(x):                                 # Define the function
    count = 0                                        # set up the counter
    for char in x:                                   # Loop through each character
        if char== 'a' or char== 'e' or \
       char== 'i' or char=='o' or char=='u':         # Check if the character is a vowel or not
            count += 1
    return count
print(count_vowels('Rest in peace my little Peaceful'))  #Print the result with an example 


# Second way to do it
def count_vowels(z):
    vowels = "aeiouAEIOU"
    count = 0
    for char in z :
        if char in vowels :
            count += 1
    return count
print(count_vowels("Dead does not stop love"))




    
