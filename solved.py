import unittest

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

class TestEuler(unittest.TestCase):
	def test_problem1(self):
		self.assertEqual(problem1(10, [3, 5]), 23)
		self.assertEqual(problem1(16, [3, 5]), 60) # duplicate number
		
if __name__ == '__main__':
	unittest.main()

# print("Problem 1 : %d" %  problem1(1000, [3, 5]))
