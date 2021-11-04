def Ordering():


    Menu = {"Burger": 2.50, "Fries": 2.00, "Pizza": 10, "Coke": 2.30, "Fanta": 2.20, "Cookies": 1.50}

    Menu2 = ["Burger", "Fries", "Pizza", "Coke", "Fanta", "Cookies"]

    Decision = {"Yes": 1, "No": 2}

    Price = 0

    Total = 0

    Counter = 1

    #x = ""

    #y = ""

    #z = ""

    while Counter == 1:

        Selection = input("Enter your selection: ")
        Price = Menu.get(Selection)
        print(Price)

        Counter = Decision.get(input("Continue? "))



        if Price >= 0:
            Total = Total + Price

            print (Total)





            #if Price == 2.00:
               # x = "Fries"

            #else:
               # pass


            #if Price == 2.20:
               # y = "Fanta"

            #else:
                #pass

            #if Price == 10:
                #z = "Pizza"









    else:
        print ("You have ordered", Selection)
        #print ("You have ordered", x, y, z)
        print("Your Order has been confirmed and it will cost", Total, "euro")


# Counter to add 2 to any double orders , IF statement for if fries etc pressed)



Ordering()

#Order confirmation and review section  Delivery message and
