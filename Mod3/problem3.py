'''
Prompt the user for a sentence and a word to try to find in that sentence.
Have the program print out whether the word was found in the sentence. (i.e. True or False)
'''
sentence = input("can you please type a sentence?")
word_to_search = input ("can you please provide a word to search in your sentence?")
print(word_to_search in sentence)

