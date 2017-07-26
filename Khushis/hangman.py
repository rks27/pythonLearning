print("let's play hangman")
word = ["d", "i","c","t","i","o","n","a" ,"r","'y"]
blank = ['__','__','__','__','__','__','__','__','__','__',]
tries = 6
guess = False
n = 0
nn = 0
while tries>1 and guess == False:
  userinput = str(input("Enter a letter"))
  for i in range (len(blank)):
      if word[i] == userinput:
        blank[i] = userinput
  print(blank)
  if userinput is word :
      print("You lost a life")
        
          
