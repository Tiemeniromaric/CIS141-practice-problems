'''
Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''

yea_count=nay_count=0                   #Triggering the counter

with open('poll.txt','r') as file:      #Opening the file in read mode
    votes = file.read().split(',')      #saving the file content in a variable and split it 
for vote in votes:                      #Loop in the file 
    if vote == 'yea':
        yea_count += 1
    elif vote == 'nay':                 #Condition verification and count additionning
        nay_count +=1
print(f"{yea_count} votes for yea\n{nay_count} votes for nay")      #Displaying results
print(f"For a total of {yea_count+nay_count} voters")
    
