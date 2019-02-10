a = int(input("What number do you want to start with? "))
b = int(input("What number do you want to end with? "))
c = int(input("What is the interval? "))

print("Following code is using range. Khushi :D ")
for x in range(a,b,c):
    print(x)

print("Following code is using while. ")
while b > a:
    print(a)
    a = a + c

print("Khushi is the best!")