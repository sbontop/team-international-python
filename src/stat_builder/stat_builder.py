import src.util.constants as constants_service
import src.util.validators as validator_service
from collections import defaultdict


class StatBuilder:
    """
    This is a class to perform mathematical operations on integers.
    """

    def __init__(self, data: list[int]) -> None:
        """
        The constructor for StatBuilder class

        Parameters:
            data: The data to be used to build the stats.

        Returns:
            None
        """
        self.data = data
        self.stats = self.build_stats()

    def build_stats(self) -> dict[str, int]:
        """
        The function to build the stats object.

        Returns:
            dict[str, int]: The stats object.

        """
        self.data.sort()
        # Create a dictionary of the number of values greater than a given number.
        ## Part 1: Populate the dictionary with values <= the max value from input data.
        greater: dict[int: list] = {}
        i = 0
        j = 0
        while i < constants_service.MAX_VALUE and j < len(self.data):
            input_element = self.data[j]
            series_element = i + 1
            if series_element < input_element:
                greater[series_element] = self.data[j:]
                i += 1
            elif series_element == input_element:
                greater[series_element] = self.data[j + 1:]
                i += 1
            else:
                if i == constants_service.MAX_VALUE - 1 and j == len(self.data) - 1:
                    greater[series_element] = []
                j += 1
        ## Part 2: Populate the dictionary with values > the max value from input data.
        greater |= {
            x: greater[self.data[-1]]
            for x in range(self.data[-1] + 1, constants_service.MAX_VALUE + 1)
        }

        # Create a dictionary of the number of values less than a given number.
        ## Part 1: Populate the dictionary with values <= the max value from input data.
        less = {}
        i = 0
        j = 0
        while i < constants_service.MAX_VALUE and j < len(self.data):
            input_element = self.data[j]
            series_element = i + 1
            if series_element < input_element:
                less[series_element] = self.data[:j]
                i += 1
            elif series_element == input_element:
                less[series_element] = self.data[:j]
                i += 1
                j += 1
            else:
                j += 1
        ## Part 2: Populate the dictionary with values > the max value from input data.
        less |= {
            x: less[self.data[-1]]
            for x in range(self.data[-1] + 1, constants_service.MAX_VALUE + 1)
        }

        return {
            "less": less,
            "greater": greater,
        }

    def less(self, n: int) -> int:
        """
        The function to get the number of values less than a given number.

        Parameters:
            n: The number to compare the values to.

        Returns:
            int: The number of values less than the given number.
        """
        validator_service.Validator.validate_input(n)
        try:
            return len(self.stats["less"][n])
        except KeyError:
            return 0

    def greater(self, n: int) -> int:
        """
        The function to get the number of values greater than a given number.

        Parameters:
            n: The number to compare the values to.

        Returns:
            int: The number of values greater than the given number.
        """
        validator_service.Validator.validate_input(n)
        try:
            return len(self.stats["greater"][n])
        except KeyError:
            return 0

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
        validator_service.Validator.validate_input(n1)
        validator_service.Validator.validate_input(n2)
        validator_service.Validator.validate_range(n1, n2)
        return len(
            set(self.stats["greater"][n1]).intersection(set(self.stats["less"][n2]))
        )
