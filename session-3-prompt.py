import numpy as np

def f(x): # Creates and defines the function f(x)
	x = 9 #Creates the value of x to 9 so we can find what y is at x = 9
	y = x**3 + 8 #Creates the integer y
	if y > 27: #Checks if y is larger than 27 if so executes
		print("YAY!") #Prints yay
		return y;
	else: #If y < 27 then in prints womp womp as that is sad.
		print("womp womp")

f(x) #executes the function f(x)
