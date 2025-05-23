'''
In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
simple type effectiveness rules. Your solution only needs to work for these three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''
def type_advantage(attacker,defender):                      # Define the function
    
    if attacker == "Water" and defender == "Fire":          # Open the statements
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    else:
        return "Unknow"                                     # close the statements
        
print(type_advantage("Water","Fire"))                       # Call the function and prind the firts output
print(type_advantage("Fire","Water"))
print(type_advantage("Electric","Grass"))
