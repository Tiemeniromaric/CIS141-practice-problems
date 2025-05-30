'''
Create a file called gardening_tips.txt and add at least 3 gardening tips to
it. Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
  
with open('gardening_tips.txt','r') as file: #Open and read the file
    for line in file:                        # Make a loop in the file line by line
        print(line, end='')                  # Print out each line one by one
