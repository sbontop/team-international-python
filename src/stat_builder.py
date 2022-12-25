class StatBuilder:
    """
    This is a class to perform mathematical operations on integers.
    """

    def __init__(self, data: list[int]):
        """
        The constructor for StatBuilder class
        
        Parameters:
            data: The data to be used to build the stats.
            
        Returns:
            None
        """
        self.data = data
        self.stats = self.build_stats()
    
    def validate_range(self, n1: int, n2: int) -> None:
        """
        The function to validate that the range is valid.

        Parameters:
            n1: The first number in the range.
            n2: The second number in the range.

        Raises:
            Exception: The range is invalid.

        Returns:
            None
        """
        if n1 > n2:
            raise Exception(f"Invalid range, {n1} should be greater than {n2}")
            
    
    def build_stats(self) -> dict[str, int]:
        """
        The function to build the stats object.

        Returns:
            dict[str, int]: The stats object.

        """
        less = lambda n: len([x for x in self.data if x < n])
        between = lambda n1, n2: len([x for x in self.data if x >= n1 and x <= n2])
        greater = lambda n: len([x for x in self.data if x > n])
        return {
            'less': less,
            'between': between,
            'greater': greater,
        }
    
    def less(self, n: int) -> int:
        """
        The function to get the number of values less than a given number.

        Parameters:
            n: The number to compare the values to.

        Returns:
            int: The number of values less than the given number.
        """
        return self.stats["less"](n)
    
    def between(self, n1: int, n2: int) -> int:
        """
        The function to get the number of values between two given numbers.

        Parameters:
            n1: The first number in the range.
            n2: The second number in the range.

        Raises:
            Exception: The range is invalid.

        Returns:

            int: The number of values between the given numbers.
        """

        self.validate_range(n1, n2)
        return self.stats["between"](n1, n2)
    
    def greater(self, n: int) -> int:
        """
        The function to get the number of values greater than a given number.

        Parameters:
            n: The number to compare the values to.

        Returns:
            int: The number of values greater than the given number.
        """

        return self.stats["greater"](n)
