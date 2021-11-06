#Delivery App - Lauren Igoe, Patrick Tobin, Jack Leonard 
import pandas
from pandas import *

################################ Menu + Orders Data Store 
# importing module
from pandas import *

# reading CSV file
data = read_csv("food_menu.csv")
data2 = read_csv("past_orders.csv")

# converting column data to list
Food = data['Food'].tolist()
Price = data['Price '].tolist()



# printing list data
print('Food:', Food)
print('Prices:', Price )

Menu = dict(zip(Food, Price))
#print(Menu)


################################


############################### USer Profile 

class user:
    pass

user1 = user()



profile = []
def signin(name, number, address) :
    p = (name, number, address)
    profile.append(p)
    print(name, number, address)
    print(profile)
    Correct_detais = input("Are these details correct?:")
    if Correct_detais == "yes":
        print("Thank you! Details confirmed")




################################# App Init 

print("------------------------")
print('|                       |')
print('|    Welcome to the     |')
print('|    Delivery App!      |')
print('|                       |')
print("------------------------")
print("Please enter your details to make an order!")
name = input("Please enter your first and last name:")
number = input ("Please enter your number:")
address = input("Please enter your address:")
signin(name, number, address)
user1.name = name 
user1.number = number 
user1.address = address


################################# Ordering Func 

def Ordering():
    # Dictionary containing the items on the menu and their correpsonding prices

    print("Check out the menu: ")
    print('─' * 10)
    for food, price in Menu.items():
      print('{} | €{}'.format(food, price))
    print('─' * 10)



    Menu2 = ["Burger", "Fries", "Pizza", "Coke", "Fanta", "Cookies"]
    # List of all items of the menu

    Order = []
    # Empty list to assign user input into

    Decision = {"Yes": 1, "No": 2}
    # Dictionary containing two expected user inputs and assignning values to them allowing the user inouts to be implemented into different loops


    Price = 0

    Total = 0

    Counter = 1

    # Giving variables beginning values. Counter was given the value 1 so the while loop would take place straight away


    while Counter == 1:

        Selection = input("Enter your selection: ")
        if Selection in Menu:
            Price = Menu.get(Selection)
        # Taking the user input and assigning the variable associated with it to the Price variable
            print(Selection, Price)
        # Prints users Seletion and Price

            Order.append(Selection)
            print(Order)
            

            Counter = Decision.get(input("Continue?(Yes/No) "))
            # Adds user input to the empty list and prints the list

            # User recieves the option to Continue. Answering with Yes or No changes the Counters value

        else:
            break




        if Price >= 0:
            Total = Total + Price


            print (Total)
        # Adding each price to the total for the order



    else:
        print ("You have ordered", Order)
        # If the user does not want to continue the Order will print

        Counter = Decision.get(input("Do you wish to confirm this order(Yes/No): "))
        # User inputs confirms if they want to confirm the order

        if Counter == 1:
            print("Your Order will cost £" ,Total)

        else:
            print("Please place your order again")
    user1.selection = Selection
Ordering()

payment_type = ""
card_number = ""
def payment():
    print("Please select your payment method")
    payment_type = input("Card/Cash: ")
    if payment_type == "Card":
        card_number == input("Please input card number to complete online payment: ")
        print("Payment successful, you order will be delivered in approxiamtely 30 minutes")
    else:
        print("Please have the cash ready at the door for the delivery driver ")
        
payment()


############ Save it all to a datestore 
with open('past_orders.csv','a') as fd:
  fd.write(user1.name + user1.selection)




