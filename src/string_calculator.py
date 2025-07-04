import re

class StringCalculator:
    """
    A simple calculator that adds numbers from a string.
    The string may contain numbers separated by commas, newlines, or a custom delimiter.
    """

    def __init__(self):
        """
        Initializes the StringCalculator instance.
        """
        self._add_called_count = 0

    def add(self, numbers: str) -> int:
        """
        Adds numbers from a string using default (comma, newline) or custom delimiters.

        Args:
            numbers (str): The input string containing the numbers and optional delimiter.

        Returns:
            int: The sum of the numbers. Returns 0 for an empty string.
        """
        self._add_called_count += 1  # Increment counter
        if not numbers:
            return 0

        cleaned_string = self.extract_numbers_string(numbers)
        delimiters = self.get_delimiters(numbers)
        return self.calculate_sum(cleaned_string, delimiters)

    def extract_numbers_string(self, numbers: str) -> str:
        """
        Extracts the numeric portion of the string, removing any delimiter declaration.

        Args:
            numbers (str): Full input string (may include delimiter declaration).

        Returns:
            str: The actual string of numbers to be processed.
        """
        if numbers.startswith("//"):
            return numbers.split("\n", 1)[1]
        return numbers

    def get_delimiters(self, numbers: str) -> list[str]:
        """
        Determines the delimiters based on the input.

        Args:
            numbers (str): The input string.

        Returns:
            List[str]: A list of delimiters to be used for splitting.
        """
        if numbers.startswith("//"):
            delimiter_declaration = numbers.split("\n", 1)[0]
            custom_delimiter = delimiter_declaration[2:]  # works for single-character delimiters
            return [re.escape(custom_delimiter)]
        return [",", "\n"]

    def calculate_sum(self, numbers: str, delimiters: list[str]) -> int:
        """
        Splits the input numbers string using the given delimiters and returns the sum.

        Args:
            numbers (str): The cleaned string of numbers.
            delimiters (List[str]): List of delimiters to use for splitting.

        Returns:
            int: The sum of the integers found.
        """
        pattern = "|".join(delimiters)  # create regex pattern: e.g. ",|\n|;"
        tokens = re.split(pattern, numbers)
        #finding a negative number and calculating total
        negatives = []
        total = 0
        for token in tokens:
            if token:
                num = int(token)
                if num < 0:
                    negatives.append(str(num))
                total += num

        if negatives:
            raise ValueError(f"negatives not allowed: {','.join(negatives)}")

        return total
    
    def get_called_count(self) -> int:
        """
        Returns how many times the add() method was called.
        """
        return self._add_called_count
