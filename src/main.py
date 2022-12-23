class DataCapture:
    """
    This is a class to perform mathematical operations on integers.
    """

    def __init__(self) -> None:
        """
        The constructor for DataCapture class. 
        """

        self.data = []
    
    def validate_input(self, input) -> None:
        """
        The function to validate that input is an integer and positive.

        Parameters:
            input: The value to be validated as an integer.
        
        Raises:
            Value Error (Exception): The input is not an integer or is negative.

        Returns:
            None
        """

        if not isinstance(input, int):
            raise ValueError('Only integers are allowed')
        if input < 0:
            raise ValueError('Only positive integers are allowed')
        

    def add(self, number) -> None:
        """
        The function to add a number to the data list.
        
        Parameters:
            number: The number to be added to the data list.

        Raises:
            Value Error (Exception): The input is not an integer or is negative.

        Returns:
            None
        """

        self.validate_input(number)
        self.data.append(number)
    
    def build_stats(self) -> None:
        """
        The function to build the stats object.

        Returns:
            StatBuilder: The stats object.
        """

        return StatBuilder(self.data)

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
    
if __name__ == '__main__':
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(3)
    capture.add(4)
    capture.add(5)
    print(f"Capture: {capture.data}")
    stats = capture.build_stats()
    print(f"Values less than 4: {stats.less(4)}")
    print(f"Values between 2 and 4: {stats.between(2, 4)}")
    print(f"Values greater than 3: {stats.greater(3)}")
