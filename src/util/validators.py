from src.util import constants as constants_service
from src.util import exceptions as exceptions_service


class Validator:
    """
    The class to validate the input.
    """

    @staticmethod
    def validate_input(input) -> None:
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
            raise ValueError("Only integers are allowed")
        if input < 0:
            raise ValueError("Only positive integers are allowed")
        if input > constants_service.MAX_VALUE:
            raise exceptions_service.InvalidInputExceedMaxError(
                input, constants_service.MAX_VALUE
            )

    @staticmethod
    def validate_range(n1: int, n2: int) -> None:
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
            raise exceptions_service.InvalidRangeGreaterError(n1, n2)
        if n1 + 1 == n2:
            raise exceptions_service.InvalidRangeGreaterAtLeastByOneError(n1, n2)
