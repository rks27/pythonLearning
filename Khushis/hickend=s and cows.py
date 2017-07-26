##heads=int( input("How many heads are there?"))
##legs =int( input("How many legs are there?"))
##addition = (heads+legs)
##
##something = (addition% 5 )
##print(str(something)  + "Cows")
##something1 = (something %3)
##print(str(something1) + "Chickens")


numheads = int( input("How many heads are there?"))
numlegs = int( input("How many legs are there?"))
solution = False

for c in range(numheads + 1):
    for h in range(numlegs + 1):
        if c + h == numheads  and 4*c + 2* h == numlegs:
            print("There are "+ str(c) + " Cows and " + str(h) +" Chickens")
            solution = True
if solution == False:
    print("This is not possible")


