class StringCalculator:
    """A simple string calculator that can add numbers represented as a string.
    The string can contain numbers separated by commas or empty string.
    """
    def add(self,numbers:str)->int:
        """
        Adds numbers from a comma-separated string.

        Args:
            numbers (str): A string containing up to two integers separated by a comma.

        Returns:
            int: The sum of the numbers in the string. Returns 0 for an empty string.
        """
        if not numbers:
            return 0
        
        list_of_numbers = numbers.split(',')

        return sum(int(num) for num in list_of_numbers)
        
    
    
        