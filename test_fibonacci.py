import unittest
from fibonacci import *

class TestValid(unittest.TestCase):
  def test_fibonacci(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(10), 55)

if(__name__ == '__main__'):
  unittest.main(verbosity=2)