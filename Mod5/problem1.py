# Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

n = int(input("can you please provide any positif number without a decimal part?"))
total = 0
i = 1
while i<= n:
    total += i
    i += 1
print("The sum of numbers from 1 to", n, "is:", total)
