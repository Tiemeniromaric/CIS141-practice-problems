'''
Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user and print to the screen.
'''
word = input("can you please type a word?")
index1 = int( input("can you please provide the first index?"))
index2 = int( input("can you please provide the last index?"))
print(word[index1:index2])

