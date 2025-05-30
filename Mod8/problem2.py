'''
Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
with open('hiking_log.txt','w') as file:    #This is to erase the file content each time the code is run
    file.write('')
    
while True:                                 # While loop statement to prompt the user repeatedly
    name = input('What is your hike name?(enter 0 to exit): ')          #Prompt the users for their name
    if name == '0':
        break
    distance = float(input('what is your milage?(enter 0 to exit): '))  #Prompt the users for their distances
    if distance == 0:
        break
    with open('hiking_log.txt','a') as file:                    #Open the file in append mode
        file.write(f"{name}, you did {distance} mile(s)\n")     #Append or write all this argument in the file
        
print('\n---All Your Trips---')
with open('hiking_log.txt','r') as file:                        #open the file in read mode
    print(file.read())                                          #Display the file content
    

    
