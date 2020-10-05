x=input('Enter the first number: ')
y=input('Enter the second number: ')
z=input('Enter the third number: ')

if (x<y):
	if(y==z):
		print('Enter three different numbers. The secodn and the third number are equal.')
	elif(y<z):
		print('The middle number is '+str(y))
	else:
		if(x<z):
			print('The middle number is '+str(z))
		elif (x==z):
			print('Enter three different numbers. The first and the third numbers are equal')
		else:
			print('The middle number is '+str(x))
elif(x==y):
	print('Enter three different numbers. The first two numbers are the same')
elif(x<z):
		print('The middle number is '+str(x))
else:
	print('The middle number is '+str(z))
	