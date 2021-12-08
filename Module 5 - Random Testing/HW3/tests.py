# Name: Casey Levy
# CS 362 - HW 3 - Random Testing
# Description: Creating random tests for credit_card_validator


from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):
    def test_bug1(self):
        for x in range(0, 100000):
            card_num = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(card_num)

    def test_bug2(self):
        for x in range(0, 1000):
            card_num = random.randint(340000000000000, 379999999999999)
            credit_card_validator(card_num)

    def test_bug3(self):
        for x in range(0, 500):
            card_num = random.randint(0000000000000000, 9999999999999999)
            credit_card_validator(card_num)

    def test_bug4(self):
        for x in range(0, 1000):
            card_num = random.randint(5100000000000000, 5599999999999999)
            credit_card_validator(card_num)

    def test_bug5(self):
        for x in range(0, 1000):
            card_num = random.randint(2221000000000000, 2720999999999999)
            credit_card_validator(card_num)

if __name__ == '__main__':
    unittest.main()
