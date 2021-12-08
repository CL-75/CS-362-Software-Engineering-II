# Name: Casey Levy
# CS 362 - HW2 - White Box Testing
# Description: Tests for White Box Testing practice
# Test code inspired from HW2 Canvas page:
# https://canvas.oregonstate.edu/courses/1810943/assignments/8334618?module_
#    item_id=20728343

from contrived_func import contrived_func
import unittest


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertTrue(contrived_func(145))

    def test_2(self):
        self.assertFalse(contrived_func(6))

    def test_3(self):
        self.assertTrue(contrived_func(75))

    def test_4(self):
        self.assertTrue(contrived_func(5))

    def test_5(self):
        self.assertTrue(contrived_func(49))

    def test_6(self):
        self.assertFalse(contrived_func(161))

    def test_7(self):
        self.assertTrue(contrived_func(555))


if __name__ == '__main__':
    unittest.main()
