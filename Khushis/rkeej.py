bank =(input("Enter how many times a year you want to have your interest. Enter monthly, quarterly, or yearly."))
principal = float(input("Enter how much money you want to invest"))
interest = 0
if bank == "monthly":
    interest =  .5
elif bank == "quarterly":
    interest =  .10
else:
    interest = .5
    
age = (input("A = in college B = seinior citizin C = veterain D = teen E = none of the above."))
if age == 'A':
    print(interest%5 )
elif age == 'B':
    print(interest%20)
elif age == 'C':
    print(interest%20 )
elif age == 'D':
    print(interest%0 )
else:
    print(interest )

    
