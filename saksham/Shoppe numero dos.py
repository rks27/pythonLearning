#Saksham Singh
#Shopping program
#First edit: 12/15/18
#Last edit: 12/15/18

#introducing the program
x = 1
realcost  = 0
#receipt printing function
def totals():
    cost = 0
    cost = cost + realcost
    tax = 0
    totalc = 1
    tax = cost * 0.09
    totalc = totalc + tax + cost
    tax = str(tax)
    cost = str(cost)
    totalc = str(totalc)
    print("Tax:" + " " + "$" +tax + " " + "Shipping: $1")
    print(" ")
    print("______________________")
    print(" ")
    print("Cost: " + "$" + cost)
    print(" ")
    print("______________________")
    print(" ")
    print("End total: " + "$"  + totalc  )
    return
#The whole program runs on this loop
while x == 1:
    print("---|-------------------------------------------------|---------")
    print("    ___|___                                            ___|___ ")
    print("   ////////\   _                                   _  /\\\\\\\\")
    print("  ////////  \ ('<                               >') /  \\\\\\\\")
    print("      | (_)  |  | (^)                           (^) |  | (_)  |")
    print("  |______|.======                ======.|______|")
    print("---------------------------------------------------------------")
    print(" ")
    print(" ")
    print(" ")
    print("                                         Hello valued customer!                                     ")
    print("                                      This is a shopping website                                      ")
    print("                                           called CABABAZON                                             ")
    print(" ")
    print(" ")
    print("---------------------------------------------------------------  ")
    choice = input("Would you like to buy something today? ")
    choice = choice.upper()
    #making a str choice readable by the idiotic computer
    if choice == "NO":
        print(" ")
        print(" ")
        print("---------------------------------------------------------------  ")
        print("OK, Have a good day")
        print("---------------------------------------------------------------  ")
        x= 2
    elif choice == "YES":
        #The whole shopping part runs on this loop
                z = 1
                while z == 1:
                    print(" ")
                    print(" ")
                    print("---------------------------------------------------------------  ")
                    print("                                                             |                                                                   ")
                    print("                For Fresh Food               |                      For Necessities                ")
                    print("                 Enter 1                              |                         Enter 2               ")
                    print("                                                             |                                                                ")
                    print("---------------------------------------------------------------  ")
                    print("---------------------------------------------------------------  ")
                    print("                                                             |                                                                       ")
                    print("                For Technology              |                      For Clothes                  ")
                    print("                 Enter 3                              |                         Enter 4               ")
                    print("                                                             |                                                                 ")
                    print("---------------------------------------------------------------  ")
                    print("---------------------------------------------------------------  ")
                    print("                                                             |                                                                       ")
                    print("                For Furniture                   |                       For Sodas                  ")
                    print("                 Enter 5                              |                         Enter 6               ")
                    print("                                                             |                                                                 ")
                    print("---------------------------------------------------------------  ")
                    #What category they want to buy from
                    buychoice = int(input("So, what will it be : "))
                    if buychoice ==1:
                    #An array of inputs for what they want to buy from each category
                        customfood = input("What food would you like to buy? ")
                        print("Good choice, that will be $20")
                        realcost = realcost + 20
                    if buychoice == 2:
                        customfood = input("What necessity would you like to buy? ")
                        print("Good choice, that will be $15")
                        realcost = realcost + 15
                    if buychoice == 3:
                        customfood = input("What technology would you like to buy? ")
                        print("Good choice, that will be $500")
                        realcost = realcost + 500
                    if buychoice == 4:
                        customfood = input("What clothe(s) would you like to buy? ")
                        print("Good choice(s), that will be $25")
                        realcost = realcost + 25
                    if buychoice == 5:
                        customfood = input("What furniture would you like to buy? ")
                        print("Good choice, that will be $1200")
                        realcost = realcost + 1200
                    if buychoice == 6:
                        customfood = input("What soda would you like to buy? ")
                        print("Good choice, that will be $5")
                        realcost = realcost + 5
                    print("---------------------------------------------------------------  ")
                    #creating a part that can end all of the loops and print/not print a reciept
                    shoppingchoice = input("Enter yes to keep shopping or no to end your trip: ")
                    shoppingchoice = shoppingchoice.upper()
                    if shoppingchoice == "YES":
                        continue
                    if shoppingchoice == "NO":
                        z = 2
                        x = 2
                        print(" ")
                    print(" ")
                    print("---------------------------------------------------------------  ")
                    choice2end = input("Would you like to see your reciept? ")
                    choice2end = choice2end.upper()
                    if choice2end == "YES":
                        print("Here it is!")
                        #reciept function from before
                        totals()
                    if choice2end == "NO":
                        print("Ok then")
                    nothing = int(input("Enter you credit card number to pay: "))
                    print("Thank you!")
                    print("---------------------------------------------------------------  ")
    else:
        y = 1
        while y == 1:
            #Idiot proof entry system
            choice = input("I am very sorry, but that is no a valid choice. Try yes or no: ")
            choice = choice.upper()
            if choice == "NO":
                y = 2
                print(" ")
                print(" ")
                print("---------------------------------------------------------------  ")
                print("OK, Have a good day")
                print("---------------------------------------------------------------  ")
                x = 2
            if choice == "YES":
                y = 2
                z = 1
                while z == 1:
                    #Exact same things as before, just entered into the idiot-proof part
                    print(" ")
                    print(" ")
                    print("---------------------------------------------------------------  ")
                    print("                                                             |                                                                   ")
                    print("                For Fresh Food               |                      For Necessities                ")
                    print("                 Enter 1                              |                         Enter 2               ")
                    print("                                                             |                                                                ")
                    print("---------------------------------------------------------------  ")
                    print("---------------------------------------------------------------  ")
                    print("                                                             |                                                                       ")
                    print("                For Technology              |                      For Clothes                  ")
                    print("                 Enter 3                              |                         Enter 4               ")
                    print("                                                             |                                                                 ")
                    print("---------------------------------------------------------------  ")
                    print("---------------------------------------------------------------  ")
                    print("                                                             |                                                                       ")
                    print("                For Furniture                   |                       For Sodas                  ")
                    print("                 Enter 5                              |                         Enter 6               ")
                    print("                                                             |                                                                 ")
                    print("---------------------------------------------------------------  ")
                    buychoice = int(input("So, what will it be : "))
                    if buychoice ==1:
                        customfood = input("What food would you like to buy? ")
                        print("Good choice, that will be $20")
                        realcost = realcost + 20
                    if buychoice == 2:
                        customfood = input("What necessity would you like to buy? ")
                        print("Good choice, that will be $15")
                        realcost = realcost + 15
                    if buychoice == 3:
                        customfood = input("What technology would you like to buy? ")
                        print("Good choice, that will be $500")
                        realcost = realcost + 500
                    if buychoice == 4:
                        customfood = input("What clothe(s) would you like to buy? ")
                        print("Good choice(s), that will be $25")
                        realcost = realcost + 25
                    if buychoice == 5:
                        customfood = input("What furniture would you like to buy? ")
                        print("Good choice, that will be $1200")
                        realcost = realcost + 1200
                    if buychoice == 6:
                        customfood = input("What soda would you like to buy? ")
                        print("Good choice, that will be $5")
                        realcost = realcost + 5
                    print("---------------------------------------------------------------  ")
                        
                    shoppingchoice = input("Enter yes to keep shopping or no to end your trip: ")
                    shoppingchoice = shoppingchoice.upper()
                    if shoppingchoice == "YES":
                        continue
                    if shoppingchoice == "NO":
                        choice2end = input("Would you like to see your reciept? ")
                        choice2end = choice2end.upper()
                    if choice2end == "YES":
                        print("Here it is!")
                        totals()
                    if choice2end == "NO":
                        print("Ok then")
                    nothing = int(input("Enter you credit card number to pay: "))
                    print("Thank you!")
                    print("---------------------------------------------------------------  ")

                                   
                        

                        

