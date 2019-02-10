import time
import sys
print("Hi, I am a random program made for my sister's programming class")
time.sleep(2)
print("I was made by Saksham, so you will have to know a few facts about him")
time.sleep(2)
print("The first chunk will be rapid fire questions you only have 30 seconds to answer (caps don't matter)")
time.sleep(3)
print("Click enter when you are ready!")
time.sleep(1)
print("BTW, I am Khushi's brother")
print(" ")
input()
print("_______________________________________________")
print(" ")
max_time =30
start_time = time.time()  # remember when we started
while (time.time() - start_time) < max_time:
    points = 0
    name = input('What is my name(hint: it may or may not be Saksham): ')
    name = name.upper()
    if name == 'SAKSHAM':
        print("Good job!")
        print(" ")
    else:
        print("YOU WERE NEVER SUPPOSED TO FAIL THIS PART! YOU ARE STUPID")
        print(" ")
        sys.exit()
    chocolate = input('What is my favorite brand of chocolate bar')
    chocolate = chocolate.upper()
    if chocolate == 'TWIX':
        print("Good job!")
        print(' ')
        points = points + 1
    else:
        print('Nice try, but no')
        print(' ')
    harrypotter = input('What is my favorite harry potter character? ')
    harrypotter = harrypotter.upper()
    if harrypotter == 'DOBBY':
        print("Good job!")
        print(' ')
        points = points + 1
    else:
        print('Nice try, but no')
        print(' ')
    tennisage = input('What age was I when I won my first tournament?')
    tennisage = tennisage.upper()
    if tennisage == '10':
        print("Good job!")
        print(' ')
        points = points + 1
    else:
        print('Nice try, but no')
        print(' ')
    lego= input('Where did I get my lucky lego brick?')
    lego = lego.upper()
    if chocolate == 'LEGOLAND':
        print("Good job!")
        print(' ')
        points = points + 1
        break
    else:
        print('Nice try, but no')
        print(' ')
        break
    
print(" You got " + points + "/5")
