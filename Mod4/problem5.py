'''
A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free.
Ask the user for the order total and print the total cost, including shipping.
'''

order_amont = float( input("What is your total order amont ? : $"))

if order_amont >= 50 :
    print(f"Your tocal cost is $ {order_amont :.2f}.")
    
else:
    print(f"your total cost is ${order_amont + 5:.2f}.")

