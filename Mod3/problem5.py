'''
Print 3 words with a | character (called a pipe) in between them.
Use the appropriate keyword argument in print() to do so.
'''

#Fisrt way to do it
variable1 = "Never give up!"
variable2 = variable1.split(" ")
variable3 = "|".join(variable2)
print(variable3)

#Second way to do it
var1 = "Never"
var2 = "give"
var3 = " up!"

print(var1, var2, var3, sep="|")
