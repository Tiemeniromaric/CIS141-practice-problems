'''
#5. Write a function called level_up(experience) that takes a player's experience
points and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''
def level_up(experience):               #Define the function
    
    if 0 <= experience <= 99:           #Set the statement up to check users experiences
        return "Level 1"                  
    elif 100 <= experience <= 199:
        return "Level 2"
    elif experience >=  200:
        return "Level 3"
    else:
        return "Invalide score"                         # Return the function                         
xp = int(input("what is your experience score?: "))     # Prompt the users for their scores
print(level_up(xp))                                     #Call the function and print the result
    

