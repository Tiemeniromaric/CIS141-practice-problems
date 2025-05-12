'''Write a program that continuously asks the user to input a number.
If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.
'''

while True:
    number = float(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        print("Stopping the program")
        break
    print("You entered:", number)

