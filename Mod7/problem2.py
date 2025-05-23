'''
Write a function called is_palindrome(s) that checks whether a string is a palindrome
(reads the same forward and backward, ignoring case). The function should
returns either True or False.
'''
# Fisrt solution to the problem
def is_palindrome(s):               # Set up the function
    s = s.lower()                   # Convert the string variable to lower case
    rev = s[::-1]                   # Reverse the variable
    if s == rev:                    # Check if the string is a palindrome or no
        return True
    else:
        return False
print(is_palindrome("nan"))         # Call the function and print out the result
print(is_palindrome("nana"))
print(is_palindrome("Madam"))



# Another path
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Civic"))
