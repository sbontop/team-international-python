class InvalidRangeGreaterError(Exception):
    """
    The class to handle invalid range errors.
    """

    def __init__(self, n1: int, n2: int):
        """
        The constructor for the InvalidRangeGreaterError class.

        Parameters
        ----------
        n1 : int
            The first number in the range.
        n2 : int
            The second number in the range.
        """

        self.message = f"Invalid range, {n1} should be greater than {n2}"
        super().__init__(self.message)


class InvalidRangeGreaterAtLeastByOneError(Exception):
    """
    The class to handle invalid range errors.
    """

    def __init__(self, n1: int, n2: int):
        """
        The constructor for the InvalidRangeGreaterAtLeastByOneError class.

        Parameters
        ----------
        n1 : int
            The first number in the range.
        n2 : int
            The second number in the range.
        """

        self.message = (
            f"Invalid range, {n1} should be greater than {n2} by at least one"
        )
        super().__init__(self.message)


class InvalidInputExceedMaxError(Exception):
    """
    The class to handle invalid range errors.
    """

    def __init__(self, n: int, max: int):
        """
        The constructor for the InvalidRangeExceedMaxError class.

        Parameters
        ----------
        n1 : int
            The first number in the range.
        """

        self.message = f"Invalid range, {n} should be less than {max}"
        super().__init__(self.message)


class InvalidInputError(Exception):
    """
    The class to handle invalid input errors.
    """

    def __init__(self, input):
        """
        The constructor for the InvalidInputError class.

        Parameters
        ----------
        input : int
            The value to be validated as an integer.
        """

        self.message = "Only positive integers are allowed"
        super().__init__(self.message)
