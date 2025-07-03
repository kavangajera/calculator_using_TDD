import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    """Unit tests for the StringCalculator class."""

    def setUp(self):
        """Set up the StringCalculator instance for testing."""
        self.calculator = StringCalculator()
    
    def test_add_empty_string_returns_0(self):
        """Test adding an empty string."""
        result = self.calculator.add("")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

    