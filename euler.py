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
	result = []
	max_number = number
	# for i in range(2, number+1):
	# 	if number % i == 0 and isPrime(i) == True :
	# 		result.append(i)

	for i in range(2, number + 1):
		if isPrime(i) == True and max_number % i == 0:
			result.append(i)
			max_number = max_number // i
#			print(str(i), end=' ')

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


if __name__ == '__main__':
	print("Problem 1 : %d" % problem1(1000, [3, 5]))
	print("Problem 2 : %d" % problem2(4000000))
#	print("Problem 3 : %d" % max(problem3(600851475143)))
	print("Problem 4 : %d" % problem4(3))
