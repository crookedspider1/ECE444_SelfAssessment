from math import floor

class utils():
    def _correctInput(input):
        """
        Handles inputs to ensure they are valid.
        Can handle ints, floats, and strings.
        ints: returns input
        floats: returns the floor(input)
        strings: returns the int(input)
        other: throws error
        """
        
        if type(input) is int:
            return input
        
        if type(input) is float:
            return floor(input)
        
        if type(input) is str:
            return floor(float(input))
        
        raise Exception("Invalid input.")
    
    def reversed(number) -> int:
        """
        Takes a number and returns the reverse of it.
        """
        #ensure the number is correctly formatted
        number = utils._correctInput(number)
        #convert the number to a string if it was an int
        numberString = str(number)
        #reverse the string
        reversedString = numberString[::-1]
        #convert back to int and return the result
        return int(reversedString)
    
    def formatter(number) -> tuple:
        """
        Returns a tuple containing the number formatted in base 2
        and base 8.
        """
        #ensure the number is correctly formatted
        number = utils._correctInput(number)
        #return the binary and octal forms
        return (bin(number), oct(number))
    
