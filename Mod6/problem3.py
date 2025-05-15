'''
 Create a list of strings. Write code to create a new list that includes only the strings longer than three characters.
 Print the resulting filtered list.
'''
Cameroon_Cities= ['Yde','Buea','Dschang','Dla','Bamenda','Limbe','Bafang','Nde']  #Original list of the strings
New_Cities = []                   #Empty list to store the filtered list
for char in Cameroon_Cities:      #Loop in the lsit of the original list
    if len(char)> 3:
        New_Cities.append(char)
print(New_Cities)

