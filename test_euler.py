import unittest
import euler

class TestEuler(unittest.TestCase):
	def test_problem1(self):
		self.assertEqual(euler.problem1(10, [3, 5]), 23)
		self.assertEqual(euler.problem1(16, [3, 5]), 60) # duplicate number

if __name__ == '__main__':
	unittest.main()