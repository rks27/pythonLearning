x = 1

while x < 10:
    print("|_____________________________________________________________________________|")
    print("|_____________________________________________________________________________|")
    print("|                              The dog year convert                           |")
    print("|                                 By Anounymous                               |")
    print("| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  __ _ _ _ _ _ __ _ _ _ _ _ _ _ _|")
    year=int(input("|Hello kind user! Enter the amount of years into Dog Years|:\n"))
    if year >=15:
        print("________________________________________________________________________________")
        dog_year=year-15
        bat=dog_year/7
        sat=year/15
        sbat=sat+bat
        print("Your dog year is"+ str(sbat))
    if year < 15:
        natout=year/7
        print("your dog year is"+ str(natout))
    print("|_____________________________________________________________________________|")
    print("|_____________________________________________________________________________|")
