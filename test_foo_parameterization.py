import unittest
from foo_parameterization import FooParameterization

class TestFooParameterization(unittest.TestCase):
    def test_calculate_volume(self):
        # Test case for radius = 1
        foo = FooParameterization(1)
        self.assertAlmostEqual(foo.calculate_volume(), 4.18879, places=4)

        # Test case for radius = 0
        foo = FooParameterization(0)
        self.assertAlmostEqual(foo.calculate_volume(), 0.0, places=4)

        # Test case for negative radius
        foo = FooParameterization(-2)
        self.assertAlmostEqual(foo.calculate_volume(), -33.51032, places=4)

if __name__ == '__main__':
    unittest.main()
