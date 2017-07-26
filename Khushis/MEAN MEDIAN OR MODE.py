import statistics
number=int(input("enter how many numbers you would like"))
mylist = []
malist = []
for i in range(1, number+1):
	numer21= int(input("Enter the number you would like to mean median or range or mode(#Iknowgrammer)"))
	mylist.append(numer21)
	slick=numer21*numer21/number
	cool=numer21
print(mylist)
print("The mean is" + str(slick))
if slick == cool:
        print("Your mode is"+str(numer21))
if number%2 == 0:
        buddy=mylist[int((number-1)/2)]
        friend=mylist[int((number-1)/2+1)]
        colleauge=mylist+(buddy+friend)/2
        print("Your median is" + buddy)
else:
        friend=mylist[int((number-1)/2)]
        print("Your median is" + str(median))

	
