class StringCalculator:
    """A simple string calculator that can add numbers represented as a string.
    The string can contain numbers separated by commas or empty string.
    """
    def add(self,numbers:str)->int:
        """
        Adds numbers from a string separated by commas.

        Args:
            numbers (str): A string with 0,1 or 2 integers separated by commas.

        Returns:
            int: The sum of the numbers.

            for empty string, it returns 0.
        """
        if not numbers:
            return 0
        return int(numbers) # refactor + green 
        
    
    
        