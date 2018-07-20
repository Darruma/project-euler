
num = 20
checkVal = 0

def checkDivisible(a,b):
	return (a % b == 0)

while(checkVal < 20):
	for i in range(1,20):
		if (checkDivisible(num,i)):
			checkVal = checkVal + 1	
		else:
			print(num)
			num = num + 20
			checkVal = 0
print(num)


