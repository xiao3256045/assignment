import random
f = random.randint(0, 10)
#print(str(f))
guessnumber = input('Guess the number:')
#print (str(guessnumber))
while(str(f)!=str(guessnumber)):
    print("Wrong, try again!")
    guessnumber = input('Guess the number:')
else:
    print ("Correct!")
