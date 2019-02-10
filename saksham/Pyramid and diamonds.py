#Saksham Singh
#Program for multiple uses
#Last updated: 2/9/19
##################################################
import time
import random
x = 1
whole_choice = 0
tabspace = "    "

#Permanent Functions
###################################################
#Magic ball function

def magicball():
    z = 1
    while z == 1:
        decide = input(" Enter 1 if you want me to answer your question or 2 if you dont: ")
        time.sleep(2.2)
        if decide == "1":
            blah = input("Enter your question (yes or no ones work the best): ")
            myList = ["The fates may say so", "There is a chance,", "It is what your soul says", "It is decidedly so", "Many odds are against that", "Defidently", "Never", "Of course", "Im, not sure, but your lucky number is 7", "Just follow your heart. You will get the answer", "Go ahead and forget about it", "Eh, maybe", "Dont be to confident about that","Your chances of that seem hazy", "Yes!", "The chances of that are similar to winning the lottery and getting stuck by lightning on the same day", "There is the exact same chance that your clock will reach 25:00"]
            choice = random.choice(myList)
            print(choice)
            print(" ")
            j = input("Now for the next round! ")
            time.sleep(0.25)
        if decide == "2":
            print("Have a good day!")
            print("_" * 23 )
            z = 2
            continue
    return

#Calculator function

def calculator():
    endresult = 0
    calc_use = 1
    print(" ")
    print("Hello, this is your friendly neighborhood type - based calculator!")
    time.sleep(1.3)

#Rules and guidelines

    print("This is how it works:")
    time.sleep(0.7)
    input(tabspace + "*This calculator is limited to doing an operation in between to numbers, keep that in mind!")
    input(tabspace + "*The calculator will ask for a number, and then ask for an operator before the second number")
    input(tabspace + "*Click enter to continue operating when you encounter a blank space after every two numbers you enter")
    input(tabspace + "*If you wish to stop operating, enter end")
    input(tabspace + "*That's it! Click enter to start! ")

#Creating conditions for first run of use

    while True:
        if calc_use == 1:
            calc1 = float(input("Enter a number: "))
            calcoperator = input("Enter an operator: ")
            calc2 = float(input("Enter number: "))
            if calcoperator == "*" or calcoperator == "x" or calcoperator == "X":
                endresult = endresult + (calc1 * calc2)
            if calcoperator == "+":
                endresult = endresult + calc1 + calc2
            if calcoperator == "-":
                endresult = endresult + calc1 - calc2
            if calcoperator == "/":
                endresult = endresult + (calc1/calc2)
            if calcoperator == "^":
                endresult = endresult + (calc1^calc2)
            calc_use = calc_use + 1
            choicecalc = input("")
            choicecalc = choicecalc.upper()
            if choicecalc == "END":
                False


#Creating conditions for the rest of the runs of use

        else:
            calcoperator = input("Enter an operator: ")
            calc2 = float(input("Enter number: "))
            if calcoperator == "*" or calcoperator == "x" or calcoperator == "X":
                endresult = endresult * calc2
            if calcoperator == "+":
                endresult = endresult + calc2
            if calcoperator == "-":
                endresult = endresult - calc2
            if calcoperator == "/":
                endresult = endresult / calc2
            if calcoperator == "^":
                endresult = endresult ^ calc2
            choicecalc = input("")
            choicecalc = choicecalc.upper()
            if choicecalc == "END":
                False
    print(str(endresult))
    return
    
calculator()
        
                         
while x ==1:
    whole_choice = whole_choice + 1
    if whole_choice == 1:
        print("So, here you are, you pathetic excuse for an intelligent being on thi...")
        time.sleep(3.5)
        print("Sorry, where are my manners?")
        time.sleep(0.25)
        print("I am AI bot, a small program that you can use to do fairly boring tasks and games")
        print("(Please note that this program contains no AI whatsoever)")
        time.sleep(1)
        print("(Entering will generally make the text proceed in the program)")
        time.sleep(1.3)
        input("So, let's get started, shall we!")
        print("________________________________________")
        print("|                    |                 |")
        print("|  For Magic ball    |For Triangles    |")
        print("|      Enter 1       |  Enter 2        |")
        print("________________________________________")
        print("________________________________________")
        print("|                     |                |")
        print("|  For Calculator     |For Rock Paper  |")
        print("|      Enter 3        |Scissors Enter 4|")
        print("________________________________________")
    print("You will get more choices the next round")
    time.sleep(1)
    choiceround1 = int(input("So, what will it be today!: "))
    print("Ahh, good choice")
    print("")
    print("_______________________________________________________")
    print(" ")
    time.sleep(0.5)
    if choiceround1 == 1:
        magicball()
    if choiceround1 == 2:
        y = 1
        while y == 1:
            basechoice = int(input("How long would you like the base of you triangle to be? "))
            print("Alright, construction is finished!")
            for i in range(basechoice):
                v = basechoice - i
                print(" " * v + "n" * i + " " * v )
            choicetriangle = input("Would you like to use it again? (yes or no)")
            choicetriangle = choicetriangle.upper()
            if choicetriangle == "YES":
                continue
            else:
                print("Alright, have a good one! ")
                print(" ")
                print("_"*23)
                print(" ")
                y = 2

        
                
        
            
    
    
    
