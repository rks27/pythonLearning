#Saksham Singh
#Factorials

import time
factorial = int(input("Enter the number you wish to factorial (has to be natural): "))
endfact = 1
start = 0
x = 1
while True:
    start = start + 1
    endfact = endfact * start
    if start == factorial:
        break
print("Your solution is...*drumrool* ")
endfact = str(endfact)
time.sleep(3)
print(endfact)
