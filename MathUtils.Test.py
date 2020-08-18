import unittest

import MathUtils

class MathUtilsTests(unittest.TestCase):
    def test_Sigmoid(self):
        print("Testing Sigmoid")
        self.assertEqual(MathUtils.Sigmoid(0), 0.50000)
        self.assertAlmostEqual(MathUtils.Sigmoid(-3), 0.047426, 4)

if __name__ == '__main__':
    unittest.main()