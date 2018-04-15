more = True
while more==True:
	'''Taking marks from user for marks'''
	name = raw_input("Enter your name >>>")
	maths_marks = input("Maths marks >>>")
	science_marks = input("Science marks >>>")
	english_marks = input("English marks >>>")
	comupter_marks = input("Computer marks >>>")
	total = maths_marks+science_marks+english_marks+comupter_marks
	 # using 400.0 to get faction value else if total will be less than 400(and mostly it will be) then it will be 0
	percentage = (total/400.0)*100
	print name,", your total marks is",total,"and your percentage is",percentage

	#User have to enter y if he want to run it again
	a = raw_input("Want to enter more y/n >>>")
	if a!="y":
		#if user enters other than 'y' then making 'more' to 'False' to stop the loop. As condition in while will not be satisfied then
		more = False

