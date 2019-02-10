#######################################
#Created by: Saksham singh
#purpose: Functional tennis record
#Last updated: nada
#Update purpose: nada
#date of original creation: nada
#Started: 7/24/2017
#Safety: None
#Copyright: All can use beside goats
#_____________________________________#
#######################################
#_____________________________________#
#######################################
#Naming variables
#m = match
#pl = player
#lo = losses
#######################################
#_____________________________________#
x = 1
#_____________________________________#
##dotted line(know that all the decorations took a while to perfect)
commondeco = "_ _" * 16
#_____________________________________#
##line
#_____________________________________#
deco = "_" * 48
##fancy deco
#_____________________________________#
fancy1 = "[--+--]" * 7
fancy2 = "--=--=-" *5
#_____________________________________#
#start
print(commondeco)
print(fancy2)
print("|              Python Of Tennis                            |")
print("|             Creator Saksham singh                 |")
print("|           For all things in tennis!                    |")
print(commondeco)
print(fancy2)
#_____________________________________#
#while loop for program
#_____________________________________#
while x == 1:
    print(deco)
    #ask for which style
    singles_or_doubles = input("Write sin for singles or dub for doubles:")
    if singles_or_doubles == "sin":
    #_____________________________________#
        #singles code
        print(fancy2)
        player1 = input("|Writethe name of the player you think is going to win(or any random player for||people with no opinion):|")
        print("|disclaimer: At the end the program will say if your prediction is correct|")
        print(fancy1)
        player2 = input("|Write the name of the other player:|")
        #printing the player resume
        #_____________________________________#
        #record
        print(commondeco)
        print(deco)
        print(fancy1)
        res_not = input("|Write res if you want to make the player's records, or not if not:|")
        if res_not == "res":
            #won match
            pl1_m = int(input("|Write the amount of matches that" + " " + player1 + "  " + "Has won" + ":|\n"))

            print(deco)
            #lost
            pl1_ml = int(input("Write how many matches this player has lost\n"))

            print(deco)
            #seed
            pl1_seed = int(input("Write the seed of the player or anything negative if he/she is unseeded:\n"))

            print(deco)

            #player 2
            #________________________________________________________________________________________#
            #won match
            pl2_m = int(input("|Write the amount of matches that" + " " + player2 + "Has won" + ":|\n"))

            print(deco)
            #lost
            pl2_ml = int(input("Write how many matches this player has lost\n"))

            print(deco)
            #seed
            pl2_seed = int(input("Write the seed of the player or anything negative if he/she is unseeded:\n"))

            print(deco)
            print(fancy2)

            print("Thankyou!:P")


            
            
        
        
              
