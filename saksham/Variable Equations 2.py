#Creator: Saksham Singh
#Stage: Alpha
#Purpose: 1 - 2  variable equations
#Purpose: Tell user if values are true or false
#Last update: 2/9/19
#________________________________________________________________________________________________
print("Version: Alpha")
z = 0
print("This program will tell you all of the values that are in your equation's line in between (20, 20), (-20, -20), (-20, 20), and (20, -20)")

#Asking value

coeff = float(input("Coefficient for x: "))
coeff2 = float(input("Coefficient for y: "))
operation = input("Enter the operator in between the two variables/coefficients: ")
endnum = float(input("Enter the equality: "))

#Printing the equation

print("Your equation is: " + str(coeff) + "x" + " " + str(operation) + " " + str(coeff2) + "y" + " " + "=" + " " + str(endnum))


#Making a nested loop to find values

for var1 in range (-20, 21):
    for var2 in range (-20, 21):

#Making a substitution system
        
        endvar1 = coeff * var1
        endvar2 = coeff2 * var2
        endnum = endnum * 2

#Finding out the operator

        if operation == "+":
            equation = endvar1 + endvar2
        if operation == "*" or operation =="x" or operation == "X":
            equation = endvar1 * endvar2
        if operation == "-":
            equation = endvar1 - endvar2
        if operation == "/":
            equation = endvar1/endvar2
        if operation == "^":
            equation = endvar1^endvar2
        displaycoor = "(" + str(var1) + "," + str(var2) + ") "
        if equation == endnum:
            print(displaycoor)
            z = 1

#End result

if z == 1:
    print("Are the values that work")
else:
    print("It seems that no point of your line has natural coordinates in the boundaries ... sorry")