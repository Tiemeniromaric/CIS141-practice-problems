'''
Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''
# Set the function ferry_fare
# Uses statements to check the fare  conditions
# Prompt the passengers to enter their age and whether they have a vehicle or no
# Call the function with the passengers input
# Print the result

# First way to solve the problem
def ferry_fare(age,vehicle): 
    
    if age <= 18:
        return "Your ride is free"
        
    elif 19 <= age <= 64 and vehicle == "yes":
        return "Your ride will cost $20"
    elif 19 <= age <= 64 and vehicle == "no":
        return "Your ride will cost $10"
        
    elif age >= 65 and vehicle == "yes":
        return "Your ride will cost $15"
    elif age >= 65 and vehicle == "no":
        return "Your ride will cost $5"
        
a = int(input("What is your age?: ")) 
b = input('Do you have a vehicle (yes or no)?: ').lower()
print(ferry_fare(a,b))


# Another way to solve this problem
def ferry_fare(age,vehicle):
    
    if age <= 18:
        return "Your ride is free"
        
    elif 19 <= age <= 64:
        if vehicle == "yes":
            return "Your ride will cost $20"
        else:
            return "Your ride will cost $10"
            
    elif age >= 65:
        if vehicle == "yes":
           return "Your ride will cost $15"
        else:
            return "Your ride will cost $5"

a = int(input("What is your age?: ")) 
b = input('Do you have a vehicle (yes or no)?: ').lower()
print(ferry_fare(a,b))
