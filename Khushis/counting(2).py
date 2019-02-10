a = int(input("What number do you want to start with? "))
b = int(input("What number do you want to end with? "))

print("Following code is using range. ")
name = "Khushi"
for x in range(a,b):
    print(x)

print("Following code is using while. ")
while b > a:
    print(a)
    a = a + 1
    