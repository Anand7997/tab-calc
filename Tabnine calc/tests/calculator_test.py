import os
import sys
import time

# Add the parent directory to the sys.path to ensure the calculator module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator

def test_addition():
    calc = Calculator()
    start_time = time.time()
    result = calc.addition(-3, -7)
    end_time = time.time()
    latency = end_time - start_time
    print(f"test_addition latency: {latency} seconds")
    assert result == -10


class TestCalculator:

    def setup_method(self):
        self.calc = Calculator()

    def test_addition_with_positive_integers(self):
        result = self.calc.addition(5, 7)
        assert result == 12

    def test_addition_with_floating_point_numbers(self):
        result = self.calc.addition(3.5, 2.5)
        assert result == 6.0

    def test_addition_with_positive_and_negative_integers(self):
        result = self.calc.addition(10, -3)
        assert result == 7

    def test_addition_with_mixed_types(self):
        result = self.calc.addition(5, 2.5)
        assert result == 7.5

    def test_addition_with_negative_floating_point_numbers(self):
        result = self.calc.addition(-2.5, -3.5)
        assert result == -6.0