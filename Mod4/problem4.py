'''
A theater wants to enforce age restrictions for movie tickets. Ask the user for their age,
and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17),
or R (appropriate for over 18) rated movies.
'''

# First way to resolve this problem

custumer_age = int( input("What is your age? : "))

if custumer_age < 13 :
    print("You can see G rated movies")
    
elif 13 <= custumer_age < 18 :
    print("You can see PG-13 rated movies")
    
elif custumer_age >= 18 :
    print("You can see R rated movies")


# Second way to resolve the problem

client_age = int( input("What is your age ? : "))

if client_age >= 18 :
    print("You can see R rated movies")
    
elif 13 <= client_age < 18 :
    print("You can see PG-13 rated movies")
    
else:
    print("You can see G rated movies")

