factors = []
number1 = 0
number = int(input("Enter a number"))
for i in range(1,number + 1):
    if number%i ==0:
        number1 = number1 +1
        factors.append(i)
print(factors)

factors2 = []
number10 = 0
number1 = int(input("Enter  number 1"))
num = int(input("Enter number 2"))
for j in range(1,number1 + 1):
     if number1%num ==num:
        print(num)
     elif number1%num== 2:
        print(2)
     elif  number1%num == i:
        print(str(i))
     else:
        print(number1*num)
