#Digital dice
#importing random function to genterate random number
from random import randint
print "Give lower limit of dice"
a = input()
print "Give upper limit of dice"
b = input()
print "type q to Quit or any other key/enter to continue"
while True:
	print ">>> "+str(randint(a,b))#randint is generating random number between a and b
	if raw_input() == 'q': #if 'q' is entered then come out of loop 
		break;

