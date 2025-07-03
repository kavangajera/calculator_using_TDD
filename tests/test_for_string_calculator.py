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

if __name__ == '__main__':
    unittest.main()

    