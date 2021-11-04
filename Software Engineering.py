def Ordering():
    Menu = {"Burger": 2.50, "Fries": 2.00, "Pizza": 10, "Coke": 2.30, "Fanta": 2.20, "Cookies": 1.50}
    # Dictionary containing the items on the menu and their correpsonding prices

    print("Check out the menu: ", Menu)



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
            print("Your Order has been confirmed and it will cost £" ,Total)

        else:
            print("Please place your order again")


Ordering()


