################################################
#program name: UniTec
#creator: SAksham s 21
#purpose: Young explorer assignment
#last update: 7/12/2017
#update purpose: Neatness
#comments: took a while
#simple concept
################################################
#Master loop
################################################
commondeco = "|________________________________________ |"
x=1
while x == 1:

    ########################################################
    ##Start of program
    ########################################################
    print(commondeco)
    print("|                UniTec  Systems                            |")
    print("|            Perfect For Tech and fun!                 |")
    print("|              12324 9th dr sw                              |")
    print("|                900-398-6565                                |")
    print("|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=+|-=-|")
    print("|--------------------------------------------------------|")
    ########################################################
    ##Master List
    ########################################################
    itemlist = ['lenevo', 'cpu', 'hppro', 'chewtoy', 'projector', 'xbox']
    list1 = []
    ########################################################
    #needed lookup
    ########################################################
    lookup = {'lenevo': 500.95,
              'cpu': 492.95,
              'hppro': 365.43,
              'chewtoy': 5.87,
              'projector': 999.65,
              'xbox': 99.25}
    end = 132
    ########################################################
    ##Input
    ########################################################
    index = 0
    for item in itemlist:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("For ", item)
        print("enter", index)
        product=int(input("or 234 to quit"))
        if product == index:
            index = index + 1
            print("__"*36)
            number=int(input("Write how much of that product you would like:"))
            appending=number*lookup[item]
            list1.append(appending)
        elif product == 234:
            end=index
            print("======================================================")
            break
            
    #########################################################
    ##Country area
    #########################################################
    country=input("Write WA, OR, ID, CA, NJ For country")
    print("_________________________________________________")
    print("-+_+--+_+--+_+--+_+--+_+--+_+--+_+--+_+--+_+-=_-+")
    print("-------------------------------------------------")
    #########################################################
    ##Area For price
    #########################################################
    ############################################
    ##Country
    ############################################
    if country == "WA":
        tax=0.099
        Ship=0.00
    elif country == "OR":
        tax=1
        Ship=3.00
    elif country == "ID":
        Ship=4.00
        tax=0.07
    elif country == "CA":
        tax=0.13
        Ship=5.00
    elif country == "NJ":
        tax=0.10
        Ship=10.00
    ############################################
    ##printting end
    ############################################
    if end == 132:
        #######################################
        #copying area:
        #Using for quit early
        #######################################          total                         tax                                             shipping                              real total
        print("_______________________________________")
        print(str("Lenevo ideapad:"), str(list1[0]), str("Total"), str( list1[0]), str("Tax"), str(int(float( list1[0]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[0]*tax+ list1[0]+Ship))))
        print("_______________________________________")
        print(str("CPU:"), str(list1[1]), str("Total"), str( list1[1]), str("Tax"), str(int(float( list1[1]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[1]*tax+ list1[1]+Ship))))
        print("_______________________________________")
        print(str("HP Pro:"), str(list1[2]), str("Total"), str( list1[2]), str("Tax"), str(int(float( list1[2]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[2]*tax+ list1[2]+Ship))))
        print("_______________________________________")
        print(str("Chew Toy:"), str(list1[3]), str("Total"), str( list1[3]), str("Tax"), str(int(float( list1[3]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[3]*tax+ list1[3]+Ship))))
        print("_______________________________________")
        print(str("Projector:"), str(list1[4]), str("Total"), str( list1[4]), str("Tax"), str(int(float( list1[4]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[4]*tax+ list1[4]+Ship))))
        print("_______________________________________")
        print(str("Xbox 1s:"), str(list1[5]), str("Total"), str( list1[5]), str("Tax"), str(int(float( list1[5]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[5]*tax+ list1[5]+Ship))))
        Total=( list1[0]*tax+ list1[0]+Ship)+( list1[1]*tax+ list1[1]+Ship)+( list1[2]*tax+ list1[2]+Ship)+( list1[3]*tax+ list1[3]+Ship)+( list1[4]*tax+ list1[4]+Ship)+(list1[5]*tax+list1[5]+Ship)-456
        print("Your total is(with discount)", Total)
        
        print("+=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=++=+")
    ############################################
    #printing end:
    #If quit early
    ############################################
    if end == 0:
        print("Nothing ordered")
        print("|-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-|")
    ##1#####################################          total                         tax                                             shipping                              real total
    if end == 1:
        print("_______________________________________")
        print(str("Lenevo ideapad:"), str(list1[0]), str("Total"), str( list1[0]), str("Tax"), str(int(float( list1[0]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[0]*tax+ list1[0]+Ship))))
        Total=( list1[0]*tax+ list1[0]+Ship)-2
        
        print(end)
    ##2#####################################          total                         tax                                             shipping                              real total
    if end == 2:
        print("_______________________________________")
        print(str("Lenevo ideapad:"), str(list1[0]), str("Total"), str( list1[0]), str("Tax"), str(int(float( list1[0]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[0]*tax+ list1[0]+Ship))))
        print("_______________________________________")
        print(str("CPU:"), str(list1[1]), str("Total"), str( list1[1]), str("Tax"), str(int(float( list1[1]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[1]*tax+ list1[1]+Ship))))
        Total=( list1[0]*tax+ list1[0]+Ship)+( list1[1]*tax+ list1[1]+Ship)-3
        print("Your total is(with discount)", Total)
        print("_|-~'`""'`~-|__|-~'`""'`~-|__|-~'`""'`~-|__|-~'`""'`~-|__|-~'`""'`~-|__|-~'`""'`~-|__|-~'`""'`~-|__|-~'`""'`~-|_")
    ##3#####################################          total                         tax                                             shipping                              real total(realizing the pattern?)
    if end == 3:
        print(str("Lenevo ideapad:"), str(list1[0]), str("Total"), str( list1[0]), str("Tax"), str(int(float( list1[0]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[0]*tax+ list1[0]+Ship))))
        print("_______________________________________")
        print(str("CPU:"), str(list1[1]), str("Total"), str( list1[1]), str("Tax"), str(int(float( list1[1]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[1]*tax+ list1[1]+Ship))))
        print("_______________________________________")
        
        print(str("HP Pro:"), str(list1[2]), str("Total"), str( list1[2]), str("Tax"), str(int(float( list1[2]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[2]*tax+ list1[2]+Ship))))-3
        Total=( list1[0]*tax+ list1[0]+Ship)+( list1[1]*tax+ list1[1]+Ship)+( list1[2]*tax+ list1[2]+Ship)
        print("Your total is(with discount)", Total)
        print("[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]")
    ##4#####################################          total                         tax                                             shipping                              real total
    if end == 4:
        print("_______________________________________")
        print(str("Lenevo ideapad:"), str(list1[0]), str("Total"), str( list1[0]), str("Tax"), str(int(float( list1[0]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[0]*tax+ list1[0]+Ship))))
        print("_______________________________________")
        print(str("CPU:"), str(list1[1]), str("Total"), str( list1[1]), str("Tax"), str(int(float( list1[1]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[1]*tax+ list1[1]+Ship))))
        print("_______________________________________")
        print(str("HP Pro:"), str(list1[2]), str("Total"), str( list1[2]), str("Tax"), str(int(float( list1[2]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[2]*tax+ list1[2]+Ship))))
        print("_______________________________________")
        print(str("Chew Toy:"), str(list1[3]), str("Total"), str( list1[3]), str("Tax"), str(int(float( list1[3]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[3]*tax+ list1[3]+Ship))))
        Total=( list1[0]*tax+ list1[0]+Ship)+( list1[1]*tax+ list1[1]+Ship)+( list1[2]*tax+ list1[2]+Ship)+( list1[3]*tax+ list1[3]+Ship)-4
        print("Your total is(with discount)", Total)
        print("=-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-==-_-=")
    ##5#####################################          total                         tax                                             shipping                              real total
    if end == 5:
        print("_______________________________________")
        print(str("Lenevo ideapad:"), str(list1[0]), str("Total"), str( list1[0]), str("Tax"), str(int(float( list1[0]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[0]*tax+ list1[0]+Ship))))
        print("_______________________________________")
        print(str("CPU:"), str(list1[1]), str("Total"), str( list1[1]), str("Tax"), str(int(float( list1[1]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[1]*tax+ list1[1]+Ship))))
        print("_______________________________________")
        print(str("HP Pro:"), str(list1[2]), str("Total"), str( list1[2]), str("Tax"), str(int(float( list1[2]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[2]*tax+ list1[2]+Ship))))
        print("_______________________________________")
        print(str("Chew Toy:"), str(list1[3]), str("Total"), str( list1[3]), str("Tax"), str(int(float( list1[3]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[3]*tax+ list1[3]+Ship))))
        print("_______________________________________")
        print(str("Projector:"), str(list1[4]), str("Total"), str( list1[4]), str("Tax"), str(int(float( list1[4]*tax))), str("Shipping"), str(Ship), str("Total"), str(int(float( list1[4]*tax+ list1[4]+Ship))))
        Total=( list1[0]*tax+ list1[0]+Ship)+( list1[1]*tax+ list1[1]+Ship)+( list1[2]*tax+ list1[2]+Ship)+( list1[3]*tax+ list1[3]+Ship)+( list1[4]*tax+ list1[4]+Ship)-5
        print("Your total is(and discount)"+Total)
        print("|_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_||_~-^-~_|")
    user_rec=input("Write any reccomendation keywords right here:")
    user_inp=input("Write a full review")
    print("We will try to work on", user_rec)
    review=input("We value your input. If you would like to review your input, write yes. Write anything else to end the program:")
    if review == "yes":
        print(user_inp)
        print("Thank you for using our tec shop")
        print("by saksham")
        print(commondeco)
    else:
        print("Thank you for using our tec shop!")
        print("By saksham")
    print(commondeco)
    print(commondeco)
    print(commondeco)
    print(commondeco)
    print(commondeco)
    print(commondeco)
    ########################################
    #Next program:
    #Will repeat
    ########################################
    #Thankyou for using:
    #UniTec Systems!
    ########################################





        



