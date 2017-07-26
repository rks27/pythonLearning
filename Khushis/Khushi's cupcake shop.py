#########################
#  Name:Khushi's Cupecake Shope!
#  Author: Khushi Singh
#  Date started: 7-10-2017
# History: An online cupcake shop that beats the market
# Date completed: 7-11-2017
##########################

# Header
print("-----------------------------------------------------------------")
print("            Welcome to Khushi's Cupcake Shope!")
print("           Online cupcake shopping to the max!")
print("-----------------------------------------------------------------")

#State tax
state = input("What State are you from?" +
          " WA , CA , ID , OR , NY")
dictionary = {'WA' : 0.75 , 'CA' : 0.98 , 'ID' :0.86 , 'OR' : .53 , 'NY': .79}

#Menu
print("Welcome! Here is our menu!")

print(     "_________________________________________________")
print("                                              Menu")
print("      ------------------------------------------------------------------------------")
print("              |# | Flavor                         | frosting flavors| price   |")
print("------------------------------------------------------------------------------")
menu  = input(" | 1 |Chocolate                 | Vanilla             | $0.50    |\n" 
                        "  |2 |Vanilla                      |Vanilla/choc     |$0.50     |\n" 
                       "   |3 |Red Velvet                | Cream chese    |$1.25      |\n" 
                       "   |4| Lemon cake              |Sweet Vanilla   | $1.50     |\n" 
                        "  |5|Mint                          |Chocolate         |$2.00      |\n"
            "----------------------------------------------------------------------------------" =
                          "                Enter the number you want")
num_cupcake = input("How many cupcakes would you like to purchase?")

# all the taxes
statetax("Your sales tax is " + str(state*num_cupcake))
print("Your shipping tax is 5.00")
print("Unfortunatly, today is not a holiday so there are no discounts.")

# Final recipt
tax = 5.00

print("------------------------------------------------------------------------------------------------------------")
print(" Cupcake #        Quantity          cost             Shipping tax              Tax            Total cost")
print( str(menu)+ str(num_cupcake) +str(menu)+ str(tax) +            str(statetax)+ str(menu+statetax+tax))
print("------------------------------------------------------------------------------------------------------------")
buy = input("Do you want to continue your purchase? Yes or no")
if buy == yes:
        print("Enter you credit card code.")
        print("Purchese successful. Have a wonderful day!")
else:
        print("Ok. Goodbye!")
              
                       
               
