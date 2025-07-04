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
        
        delimiters = [',', '\n']

        if numbers.startswith("//"):
            # Custom delimiter case
            parts = numbers.split('\n', 1)
            delimiter_line = parts[0]
            numbers = parts[1]
            custom_delimiter = delimiter_line[2]
            delimiters = [custom_delimiter]
        
        for d in delimiters:
            numbers = numbers.replace(d, ",")
        
        total = 0
        for part in numbers.split(","):
            if part:
                total+= int(part)
        return total


            


        return sum(int(num) for num in list_of_numbers)
        
    
    
        