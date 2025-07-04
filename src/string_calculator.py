class StringCalculator:
    """A simple string calculator that can add numbers represented as a string.
    The string can contain numbers separated by commas or empty string.
    """
    def add(self,numbers:str)->int:
        """
        Adds numbers from a string separated by commas, newlines, or a custom delimiter.

        Args:
            numbers (str): A string containing integers separated by delimiters.

        Returns:
            int: The sum of the numbers. Returns 0 for an empty string.
        """
        if not numbers:
            return 0
        
        cleaned_string = self.extract_string(numbers)
      
        delimiters = self.get_delimiter(numbers)

        total = self.calculate_sum(cleaned_string, delimiters)
        return total
    
    def extract_string(self, numbers: str) -> str:        
        """
        Extracts the string of numbers from the input, removing any custom delimiter declaration.

        Args:
            numbers (str): The input string containing numbers and possibly a custom delimiter.

        Returns:
            str: The cleaned string of numbers.
        """
        if numbers.startswith("//"):
            numbers = numbers.split("\n", 1)[1]
        if '\n' in numbers:
            numbers = numbers.replace('\n', ',')
        return numbers
    
    def get_delimiter(self, numbers: str) -> list:
        """
        Determines the delimiters used in the input string.

        Args:
            numbers (str): The cleaned string of numbers.

        Returns:
            list: A list of delimiters used in the string.
        """
        delimiters = [',', '\n']
        if numbers.startswith("//"):
            custom_delimiter = numbers.split("\n", 1)[0][2]
            delimiters.append(custom_delimiter)
        return delimiters
    
    def calculate_sum(self, numbers: str, delimiters: list) -> int:
        """
        Calculates the sum of numbers in the string using the specified delimiters.

        Args:
            numbers (str): The cleaned string of numbers.
            delimiters (list): A list of delimiters used to split the string.

        Returns:
            int: The sum of the numbers.
        """
        delimiter = ""
        for d in delimiters:
            if d in numbers:
                delimiter = d
                break
        list_of_numbers = numbers.split(delimiter)
        return sum(int(num) for num in list_of_numbers)

        
        
    
    
        