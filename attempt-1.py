def numListToInt(numList):
	s = ''.join(map(str, numList))
	return int(s)

def countNumberDigit(n):
	count=0
	while(n>0):
		count=count+1
		n=n//10
	return count

def magic(numbers=None, operators=None, prefix=""):
	for number_index in range(len(numbers)):
		if number_index!=0:
			left = numbers[:number_index]
			right = numbers[number_index:]
			for operator in operators:
				left_operator = "{}".format("{}{}".format(numListToInt(left),operator))
				right = "{}".format("{}".format(numListToInt(right)))
				express = prefix + left_operator + right
				if eval(express) == goal:
					print("{}={}".format(express, int(eval(express))))
					possibleExpresses.append(express)
				if (countNumberDigit(numListToInt(right))) > 1:
					magic(numbers=right, operators=operators, prefix=prefix + left_operator)

goal = 100
numbers = [1,2,3,4,5,6,7,8,9]
operators = ["+","-","*","/"]
possibleExpresses = []

magic(operators=operators, numbers=numbers)

print("-"*32)
print("total expresses: {}".format(len(possibleExpresses)))
print("-"*32)
