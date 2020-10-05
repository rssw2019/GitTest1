firstNumber=input('Enter the first number: ')
secondNumber=input('Enter the second number: ')

if (firstNumber==secondNumber):
	print('Enter two different numbers')
elif(firstNumber>secondNumber):
	print(str(firstNumber)+'>'+str(secondNumber))
else:
	print(str(firstNumber)+'<'+str(secondNumber))
