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
    
    def test_add_with_custom_single_one_character_semicolon_delimiter(self)->None:
        """Test adding numbers with a custom single character delimiter."""
        result = self.calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
    
    def test_add_with_custom_single_one_character_assignment_delimiter(self)->None:
        """Test adding numbers with a custom single character assignment delimiter."""
        result = self.calculator.add("//=\n1=10")
        self.assertEqual(result, 11)

    def test_add_with_string_having_one_egative_number_string_length_one(self)->None:
        """Test adding a string with one negative number in one length string."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -3")

    
    def test_add_with_string_having_one_egative_number(self)->None:
        """Test adding a string with one negative number."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-5,4")
        self.assertEqual(str(context.exception), "negatives not allowed: -5")

    def test_add_with_string_having_multiple_negative_numbers(self)->None:
        """Test adding a string with multiple negative numbers."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "negatives not allowed: -2,-4")
    
    def test_add_with_string_having_multiple_negative_numbers_with_newlines(self)->None:
        """Test adding a string with multiple negative numbers with newlines."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1\n-2,3\n-4")
        self.assertEqual(str(context.exception), "negatives not allowed: -2,-4")
    
    def test_add_with_string_having_negative_numbers_and_custom_delimiter(self)->None:
        """Test adding a string with negative numbers and a custom delimiter."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n1;-2;3;-4")
        self.assertEqual(str(context.exception), "negatives not allowed: -2,-4")
    
    def test_get_called_count_returns_number_of_add_calls(self):
        """Test that get_called_count returns the number of times add has been called."""
        self.assertEqual(self.calculator.get_called_count(), 0)  # Initially 0

        self.calculator.add("1,2")
        self.calculator.add("3")
        self.calculator.add("")

        self.assertEqual(self.calculator.get_called_count(), 3)
    
    def test_event_add_occurred_is_triggered(self):
        """Test that the event is triggered when add is called."""
        received = []

        def listener(input_str, result):
            received.append((input_str, result))

        calc = StringCalculator()
        calc.subscribe(listener)

        calc.add("1,2")
        calc.add("//;\n1;2")
        self.assertEqual(received, [("1,2", 3),("//;\n1;2", 3)])
    
    def test_add_with_numbers_greater_than_1000_ignored(self):
        """Test that numbers greater than 1000 are ignored."""
        result = self.calculator.add("1001,2,3,1000")
        self.assertEqual(result, 1005)
    
    def test_add_with_delimiter_of_any_length(self):
        """Test adding numbers with a delimiter of any length."""
        result = self.calculator.add("//[***]\n1***2***3")
        self.assertEqual(result, 6)
    
    def test_add_with_delimiter_of_any_length_mixed_characters(self):
        """Test adding numbers with a delimiter of any length with mixed chars."""
        result = self.calculator.add("//[*//*]\n1*//*2*//*3")
        self.assertEqual(result, 6)

    def test_add_with_multiple_custom_delimiters(self):
        """Test adding numbers with multiple custom delimiters."""
        result = self.calculator.add("//[;\\][**%]\n1;\\2**%4")
        self.assertEqual(result, 7)
    
   




    
    

if __name__ == '__main__':
    unittest.main()

    