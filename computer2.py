while True:
	print("Options.")
	print("Enter 'add' to add two numbers")
	print("Enter 'subract' to subtract two numbers")
	print("Enter 'multiply' to multiply two numbers")
	print("Enter 'divide' to divide two numbers")
	print("Enter 'quit'to end the program")
	user_input=input(":")
	if user_input=="quit":
		break
	elif user_input=="add":
		num1=float(input("enter a number: "))
		num2=float(input("enter another number: "))
		result=str(num1+num2)
		print("The answer is"+result)
	elif user_input=="sbtract":
		num1=float(input("enter a number: "))
		num2=float(input("enter another number: "))
		result=str(num1-num2)
		print("The answer is"+result)
	elif user_input=="multiply":
		num1=float(input("enter a number: "))
		num2=float(input("enter another number: "))
		result=str(num1*num2)
		print("The answer is"+result)
	elif user_input=="divide":
		num1=float(input("enter a number: "))
		num2=float(input("enter another number: "))
		result=str(num1/num2)
		print("The answer is"+result)
	else:
		print("Unkmow")
