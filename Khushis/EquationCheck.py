x_coef = float(input("What is the coeficent for x? "))
y_coef = float(input("What is the coeficent for y? "))
operator = input("What is the operator? ")
equality = float(input("What is " + str(x_coef) + "x" + operator + str(y_coef) + "y = ? " ))
x_value = float(input("What is the value of x? "))
y_value = float(input("What is the value of y? "))

x = (x_coef * x_value)
y = (y_coef * y_value)

result = 0

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/" :
    result = x / y
else:
    result = x + y

if result == equality:
    print("That is correct!!")
else:
    print("That's wrong. Try again.")


