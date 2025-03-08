import unittest
from src.main.assignment_3 import euler_method, runge_kutta_method, function

t0, y0 = 0, 1  # Initial conditions
t_end, steps = 2, 10  # Range and iterations
h = (t_end - t0) / steps  # Step size

class TestNumericalMethods(unittest.TestCase):
    def test_euler_method(self):
        result = euler_method(function, t0, y0, h, steps)
        expected = 1.2446380979332121
        self.assertAlmostEqual(result, expected, places=6)

    def test_runge_kutta_method(self):
        result = runge_kutta_method(function, t0, y0, h, steps)
        expected = 1.251316587879806
        self.assertAlmostEqual(result, expected, places=6)

if __name__ == "__main__":
    unittest.main()