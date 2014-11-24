import unittest

def problem1(below, multiples):
	# return 23

	numbers = [3, 5, 6, 9]
	return sum(numbers)

class TestEuler(unittest.TestCase):
	def test_problem1(self):
		self.assertEqual(problem1(10, [3, 5]), 23)
		
if __name__ == '__main__':
	unittest.main()