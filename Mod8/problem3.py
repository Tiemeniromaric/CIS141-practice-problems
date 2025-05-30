'''
Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
import string

#Initializing counters
count1 =count2 =count3 =count4 =count5 = 0

#Read file content
with open('song_lyrics.txt','r') as file:
    content = file.read()

#Removing ponctuation and convert to lower case    
content = content.translate(str.maketrans('', '',string.punctuation)).lower()

#Spliting into words
words = content.split()

#Getting inputs words from users
w1 = input('What is your first word?: ').lower()
w2 = input('What is your second word?: ').lower()
w3 = input('What is your third word?: ').lower()
w4 = input('What is your fourth word?: ').lower()
w5 = input('What is your fifth word?: ').lower()

#Statements and counts
for word in words:
    if word == w1:
        count1 += 1
    elif word == w2:
        count2 += 1
    elif word == w3:
        count3 += 1
    elif word == w4:
        count4 += 1
    elif word == w5:
        count5 += 1
        
#Creating dictionary of words and their counts
word_counts = {
    w1: count1,
    w2: count2,
    w3: count3,
    w4: count4,
    w5: count5
}

# Displaying the result
print('\n----Words Count Dictionary----')
print(word_counts)

    
    

    
