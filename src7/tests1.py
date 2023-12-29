import unittest

from prime import is_prime


class Tests(unittest.TestCase):
#class that will dericve awhole bunch of functions
    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))
        #assert false literally just asserts thatiu tis false

    def test_2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))
#assert true asserts taht ikt is true
    def test_8(self):
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """Check that 28 is not prime."""
        self.assertFalse(is_prime(28))


if __name__ == "__main__":
    unittest.main()
#this will run all of these unitvtest