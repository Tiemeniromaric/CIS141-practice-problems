'''
Prompt the user for their name and their age. Calculate their age next year.
Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
'''
user_name = input("Hello, what is your name?")
user_age = int( input("How old are you?"))
next_year_age = user_age + 1
print("Hello "+user_name +"! You are " +str(user_age)+" year (s) old. Next year, you will be "+str(next_year_age)+" years old.")

