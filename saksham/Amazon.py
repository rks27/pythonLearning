########################################################
##Start of program
########################################################
print("|______________________________________________|")
print("|              UniTec  Systems                 |")
print("|          Perfect For Tech and fun!           |")
print("|            12324 9th dr sw                   |")
print("|              900-398-6565                    |")
print("|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=|")
print("|----------------------------------------------|")
########################################################
##Master List
########################################################
lookup = {'Lenevo_ideapad': 500.95,
          'CPU': 492.95,
          'Hp_Pro': 365.43,
          'Chew_toy': 5.87,
          'Projector': 999.65,
          'Xbox_1s': 99.25}
lenevo=int(input("Write how many Lenevo Ideapads you would like(500.95):"))
########################################################
##Input
########################################################
print("_________________________________________________")
cpu=int(input("Write how many CPUs you would like(492.95):"))
print("_________________________________________________")
hp=int(input("Write how many HP_Pros you would like(365.43):"))
print("_________________________________________________")
chewtoy=int(input("Write how many dog toys you would like(5.87):"))
print("_________________________________________________")
projector=int(input("Write how many projectors you would like(999.65):"))
print("_________________________________________________")
xbox1s=int(input("Write how many Xbox 1s's you would like(99.25:"))
print("_________________________________________________")
#########################################################
##Country area
#########################################################
a=input("Write WA, OR, Id, CA, NJ For country")
print("_________________________________________________")
print("-+_+--+_+--+_+--+_+--+_+--+_+--+_+--+_+--+_+-=_-+")
print("-------------------------------------------------")
#########################################################
##Area For price
#########################################################
if lenevo > 0:
    amount1=lenevo*lookup['Lenevo_ideapad']
    print("Calculating...")
    print("_____________________________")
else:
    amount1=0
    print("None")
    print("_____________________________")
if cpu > 0:
    print("Calculating...")
    print("______________________________")
    amount2=cpu*lookup['CPU']
else:
    print("None")
    print("______________________________")
    amount2=0
if hp > 0:
    print("Calculating...")
    print("_______________________________")
    amount3=hp*lookup['Hp_Pro']
else:
    print("None")
    print("________________________________")
    amount3=0
if chewtoy > 0:
    print("Calculating...")
    print("________________________________")
    amount4=chewtoy*lookup['Chew_toy']
else:
    print("None")
    amount4=0
if projector > 0:
    print("Calculating...")
    print("_________________________________")
    amount5=projector*lookup['Projector']
else:
    print("None")
    print("__________________________________")
    amount5=0
if xbox1s > 0:
    amount6=xbox1s*lookup['Xbox_1s']
############################################
##Country
############################################
if a == "WA":
    tax=0.099
    Ship=0.00
if a == "OR":
    tax=1
    Ship=3.00
if a == "ID":
    Ship=4.00
    tax=0.07
if a == "CA":
    tax=0.13
    Ship=5.00
if a == "NJ":
    tax=0.10
    Ship=10.00
############################################
##printting end
############################################             ###Total        TAx                       TAx                          Shipping                        Total amount
print("_______________________________________")
print(str("Lenevo ideapad:"), str(lenevo), str("Total"), str(amount1), str("Tax"), str(int(float(amount1*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float(amount1*tax+amount1+Ship))))
print("_______________________________________")
print(str("CPU:"), str(cpu), str("Total"), str(amount2), str("Tax"), str(int(float(amount2*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float(amount2*tax+amount2+Ship))))
print("_______________________________________")
print(str("HP Pro:"), str(hp), str("Total"), str(amount3), str("Tax"), str(int(float(amount3*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float(amount3*tax+amount3+Ship))))
print("_______________________________________")
print(str("Chew Toy:"), str(chewtoy), str("Total"), str(amount4), str("Tax"), str(int(float(amount4*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float(amount4*tax+amount4+Ship))))
print("_______________________________________")
print(str("Projector:"), str(projector), str("Total"), str(amount5), str("Tax"), str(int(float(amount5*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float(amount5*tax+amount5+Ship))))
print("_______________________________________")
print(str("Xbox 1s:"), str(xbox1s), str("Total"), str(amount6), str("Tax"), str(int(float(amount6*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float(amount6*tax+amount6+Ship))))
Total=(amount1*tax+amount1+Ship)+(amount2*tax+amount2+Ship)+(amount3*tax+amount3+Ship)+(amount4*tax+amount4+Ship)+(amount5*tax+amount5+Ship)+(amount6*tax+amount6+Ship)
print("Your total is", Total)
print("+=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=+")






    



