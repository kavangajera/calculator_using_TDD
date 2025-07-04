import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    """Unit tests for the StringCalculator class."""

    def setUp(self)->None:
        """Set up the StringCalculator instance for testing."""
        self.calculator = StringCalculator()
    
    def test_add_empty_string_returns_0(self)->None:
        """Test adding an empty string."""
        result = self.calculator.add("")
        self.assertEqual(result, 0)
    
    def test_add_single_number_returns_number(self)->None:
        """Test adding a single number."""
        result = self.calculator.add("5")
        self.assertEqual(result, 5)
    
    def test_add_two_numbers_returns_sum(self)->None:
        """Test adding two numbers."""
        result = self.calculator.add("4,3")
        self.assertEqual(result, 7)
    
    def test_add_multiple_numbers_returns_sum(self)->None:
        """Test adding multiple numbers."""
        result = self.calculator.add("1,2,3,4,5")
        self.assertEqual(result, 15)

    def test_add_with_newlines_and_commas(self)->None:
        """Test adding numbers with newlines and commas."""
        result = self.calculator.add("1\n2,3")
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

    