import unittest
from unit_testing import avgList

# "TestCase" is parent class and "pass" is a placeholder
class TestAvgList(unittest.TestCase):
	def test1(self):
		list = [1,2,3]
		expected = 2
		self.assertEqual(avgList(list), expected, msg="avgList({})".format(list))
		# Using "assertEqual" to check if avgList produces the expected result
		# the msg portion is a message displayed if the test fails, making it easier to identify the test
		#    case that failed


	def test2(self):
		list = []
		expected = 0
		self.assertEqual(avgList(list), expected, msg="avgList({})".format(list))