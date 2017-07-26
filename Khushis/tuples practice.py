## Renember to also add plants houseing electronics  and toys

print("-----------------------------------------------------")
print("        Welcome to  Khushi's Online Store!")
print("-----------------------------------------------------")

state = input("What state are you from? " +
              "WA, OR, ID, CA, or NY.")
stuff1 = int(input("How much stuff do you want to buy?"))

stuff = input("What department woluld you like to purchase in?" +
              "Food, or Furniture")
print("-------------------------------------------------------")

if state == 'WA':
    WA = float(0.00)
elif state == 'OR':
    OR = float(.97)
elif state == 'ID':
    ID = float(.86)
elif state == 'CA':
    CA = float(.87)
elif state == "NY":
    NY = float(.23)
elif state == "none of the above":
    NOTA = float(.54)
      
for i in range(1,stuff1 + 1):
    if stuff == 'Food':
        food = input("Do you want fruits, veggitables, meats, dairy, or desserts?")
        if 'fruits':
            fruits = int(input("How many fruits do you want?"))
            lookup = {'fruits': 2.00,'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            fruits*lookup['fruits']
            print("your sales tax on that is " + str(state*fruits))
            yn = input("Do you want to continue your purchesses? Yes or no?")

            if yn == 'yes':
                    print("let's continue")
                    print("------------------------------")
            else:
                    print("Ok. Goodbye and please come back soon!")

        elif 'veggitibles':
            veggies = int(input("How many veggitibles do you want?"))
            lookup = {'fruits': 2.00 , 'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            veggies*lookup['veggitables']
            print("Your sales tax on that is " + str(state*veggies))
            yn1 = input("Do you want to continue your purchesses? Yes or no?")

            if yn1 == 'yes':
                    print("       let's continue")
                    print("--------------------------------")
            else:
                    print("Ok. Goodbye and please come back soon!")

        elif 'meats':
            meats = int(input("How much meat do you want?"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00 ,'meats':5.00 ,'dairy':3.00, 'desserts' :5.00}
            meats*lookup['meats']
            print("Your sales tax on that is " + str(states*meats))
            yn2 = input("do you want to continue? yes or no?")

            if yn2 == 'yes':
                    print("      let's go on!")
                    print("-------------------------------")
            else:
                    print("Ok. Goodbye and please come back soon!")

        elif 'dairy':
            dairy = int(input("How much dairy do you want"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            dairy*lookup["dairy"]
            print("Your sales tax is " + str(state*dairy))
            yn3 = input("do you want to continue? yes or no?")

            if yn3 =='yes':
                    print(      "Yay! let's go!")
                    print("-------------------------------")
            else:
                    print("Ok. Goodbye and come back again!")

        elif 'dessert':
            desserts = int(input("How many desserts do you want?"))
            lookup = {'fruits': 2.00, 'veggitables':3.00, 'meats':5.00, 'dairy' :3.00, 'desserts' :5.00}
            desserts*lookup["desserts"]
            print("Your sales tax is " + str(states*desserts))
            yn4 = input("Do you want to continue? yes or no?")

            if yn4 == 'yes':
                    print("  You made the right decision.")
                    print("--------------------------------") 
            else:
                    print("Ok. Goodbye and plese come back soon!")

    elif stuff == 'Furniture':

        furniture = input("What would you like to purchase. Bedroom furniture, Kitchen furniture, Outdoor furniture, livingroom furniture, or room decoration?")
        if furniture == 'Bedroom furniture':
            bfurniture = int(input("How many peices of bedroom furniture do you want?"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00, 'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            print("your sales tax is "+ str(state*bfurniture))
            yn5("Do you want to continue? yes or no?")

            if yn5 == 'yes':
                print(            "Let's continue")
                print("------------------------------------")
            else:
                print("Ok.Goodbye and plese come back soon!")

        elif furniture == 'Kitchen furniture':
            kfurniture = int(input("How many peices of kitchen furniture do you want?"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            print("Your sales tax is " + str(state*kfurniture))
            yn6 =("Do you want to continue? yes or no?")

            if yn6 == 'yes':
                  print("        let's go and shop!")
                  print("-----------------------------------")
            else:
                  print("Ok.Goodbye and plese come back soon!")
                  
        elif furniture == 'outdoor furniture':
            ofurniture = int(input("How many peices of outdoor furniture do you want?"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            print("Your sales tax is " + str(state*ofurniture))
            yn7 = ("Do you want to continue?")

            if yn7 == 'yes':
                print("              Good choice!")
                print("--------------------------------------")
            else:
                print("Ok.Goodbye. Plese come back soon")

        elif furniture == 'livingroom furniture':
            lfurniture = int(input("How many peices of livingroom furniture do you want?"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            print("Your sales tax is " + str(state*lfurniture))
            yn8 = ("Do you want to continue?")

            if yn8 == 'yes':
                print("Arn't you the smart one.")
                print("--------------------------------------")
            else:
                print("Ok.Goodbye, plese come back soon")

        elif furniture == 'room decoration':
            rfurniture = int(input("How many peices of room furniture f=do you want?"))
            lookup = {'fruits': 2.00 ,'veggitables':3.00 ,'meats':5.00 ,'dairy' :3.00 ,'desserts' :5.00}
            print("Your sales tax is " + str(state*rfurniture))
            yn9 = ("Do you want to continue?")

            if yn9 == 'yes':
                print("             Let's go!")
                print("--------------------------------------")
            else:
                print("Ok. Please come back soon.")
        
            



                



    
