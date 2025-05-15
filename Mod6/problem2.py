'''
Create a list of strings.
Write code that counts how many times the word "Olympic" appears in the list, and then print the count.
'''

Community_College = ["Bellevue","Peninsula","Olympic","Seatle","Tacoma","Olympia","Olympic"]  #List of the strings
count = 0                          #initial count
for char in Community_College:     #Loop through the list of strings
    if char == "Olympic":
        count +=1
print(count)



