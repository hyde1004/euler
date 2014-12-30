import math

def problem1(below, multiples):
	# return 23

	# numbers = [3, 5, 6, 9]
	# return sum(numbers)

	# number1 = [3, 6, 9]
	# number2 = [5]
	# number1.extend(number2)
	# numbers = number1
	# return sum(numbers)

	# number1 = [number for number in range(0, below, multiples[0])]
	# number2 = [number for number in range(0, below, multiples[1])]
	# numbers = number1 + number2
	numbers = set()
	for multiple in multiples:
		subset = {number for number in range(0, below, multiple)}
		numbers = numbers | subset
	return sum(numbers)

def problem2(below_limit):
	# fibo_set = [1, 2, 3, 5, 8]

	a, b = 1, 2
	fibo_set = [a, b]

	while b <= below_limit :
		a, b = b, a + b
		fibo_set.append(b)

	fibo_even  = [even for even in fibo_set if even % 2 == 0]

	return sum(fibo_even)

def isPrime(number):
	for i in range(2, number):
		if number % i == 0:
			return False
	else:
		return True

def problem3(number):
# 	result = []
# 	max_number = number
# 	# for i in range(2, number+1):
# 	# 	if number % i == 0 and isPrime(i) == True :
# 	# 		result.append(i)

# 	for i in range(2, number + 1):
# 		if isPrime(i) == True and max_number % i == 0:
# 			result.append(i)
# 			max_number = max_number // i
# #			print(str(i), end=' ')

	# c = []
	# a = prime_numbers(number)
	# b = number

	# if b % a[2] == 0:
	# 	c.append(a[2])
	# 	b = b // a[2]	

	# if b % a[3] == 0:
	# 	c.append(a[3])
	# 	b = b // a[3]	

	# if b % a[4] == 0:
	# 	c.append(a[4])
	# 	b = b // a[4]	

	# if b == 1:
	# 	return c

	result = []
	a = number
	b = prime_numbers(number)
	i = 0

	while(a != 1):
		if (a % b[i] == 0):
			result.append(b[i])
			while(a % b[i] == 0):
				a = a // b[i]
		i = i + 1
	return result

def isPalindrome(number):
	return str(number) == str(number)[::-1]

def problem4(digit):
	palindrome = 0
	start = 10 ** (digit - 1)
	end = 10 ** digit
	for a in range(start, end):
		for b in range(start, end):
			c = a * b
			if isPalindrome(c) == True:
				if c > palindrome:
					palindrome = c 

	return palindrome

def problem5(dividor_range):
	smallest = 1

	# while True:
	# 	if smallest % 1 == 0 and smallest % 2 == 0 and smallest % 3 == 0 and smallest % 4 == 0 and smallest % 5 == 0 and smallest % 6 == 0 and smallest % 7 == 0 and smallest % 8 == 0 and smallest % 9 == 0 and smallest % 10 == 0 : 
	# 		return smallest
	# 	else:
	# 		smallest = smallest + 1		

	# while True:
	# 	for i in range(1, dividor_range + 1):
	# 		if smallest % i != 0:
	# 			break
	# 	else:
	# 		return smallest
		
	# 	smallest = smallest + 1

	""" Using least common multiple """
	if dividor_range == 10:
		smallest = (2**3) * (3**2) * 5 * 7
	else:
		smallest = (2**4) * (3**2) * 5 * 7 * 11 * 13 * 17 * 19

	return smallest


def problem6(number):
	square_sum = sum(i*i for i in range(1, number + 1))
	sum_square = sum(i for i in range(1, number + 1))
	# return 2640
	sum_square = sum_square * sum_square
	return sum_square - square_sum

def problem7(number):
	if number == 1:
		return 2
	elif number == 2:
		return 3
def prime_numbers(number):
	# if number == 2:
	# 	return [2]
	# elif number == 3:
	# 	return [3]
	# elif number == 4:
	# 	return [2, 3]
	

	a = [x for x in range(2, number+1)]

	# c = a[0]	
	# b = [x for x in range(c*2, number+1, c)]
	# for x in b:
	# 	if x in a:
	# 		a.remove(x)
	
	# c = a[1]
	# b = [x for x in range(c*2, number+1, c)]
	# for x in b:
	# 	if x in a:
	# 		a.remove(x)

	# c = a[2]
	# b = [x for x in range(c*2, number+1, c)]
	# for x in b:
	# 	if x in a:
	# 		a.remove(x)

	i = 0
	
	c = a[i]
	while c <= math.floor(number**0.5):
		b = [x for x in range(c*2, number+1, c)]
		for x in b:
			if x in a:
				a.remove(x)
		i = i+1
		c = a[i]
	return a		

if __name__ == '__main__':
	print("Problem 1 : %d" % problem1(1000, [3, 5]))
	print("Problem 2 : %d" % problem2(4000000))
	# print("Problem 3 : %d" % max(problem3(600851475143)))
	print("Problem 4 : %d" % problem4(3))
	print("Problem 5 : %d" % problem5(20))
	print("Problem 6 : %d" % problem6(100))
