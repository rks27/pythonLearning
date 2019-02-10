#Creator: Saksham Singh
#Stage: Beta
#Purpose: 1 - 2  variable equations
#Purpose: Tell user if values are true or false
#Last update: 2/9/19
#________________________________________________________________________________________________

print("Version: Beta")
print("This program will tell you if the values you entered for an equation are true")

#Asking value

coeff = float(input("Coefficient of the first variable: "))
coeff2 = float(input("Coefficient of the second variable: "))
operation = input("Enter the operator in between the two variables/coefficients: ")
endnum = float(input("Enter the equality: "))

#Creating something for multiplying the two coefficents

endvar1 = coeff * var1
endvar2 = coeff2 * var2

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

#End result

if equation == endnum:
    print("YEEEEEEET. Those coordinates are on the line of your equation! (Those values make the equation true)! ")
else:
    print("Uh, oh. Those values don't work!")
