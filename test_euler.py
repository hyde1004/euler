import unittest
import euler

class TestEuler(unittest.TestCase):
	def test_problem1(self):
		self.assertEqual(euler.problem1(10, [3, 5]), 23)
		self.assertEqual(euler.problem1(16, [3, 5]), 60) # duplicate number

	def test_problem2(self):
		self.assertEqual(euler.problem2(10), 10)

	def test_problem3(self):
		self.assertEqual(euler.problem3(2), [2])
		self.assertEqual(euler.problem3(3), [3])
		self.assertEqual(euler.problem3(4), [2])
		self.assertEqual(euler.problem3(6), [2, 3])
#		self.assertEqual(euler.problem3(13195), [5, 7, 13, 29])

	def test_isPrime(self):
		self.assertEqual(euler.isPrime(2), True)
		self.assertEqual(euler.isPrime(3), True)
		self.assertEqual(euler.isPrime(4), False)
		self.assertEqual(euler.isPrime(5), True)
		self.assertEqual(euler.isPrime(6), False)

	def test_problem4(self):
		self.assertEqual(euler.problem4(2), (9009))

	def test_problem5(self):
		self.assertEqual(euler.problem5(10), 2520)
		self.assertEqual(euler.problem5(20), 232792560)
		
if __name__ == '__main__':
	unittest.main()