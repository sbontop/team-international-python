import src.stat_builder.stat_builder as stat_builder_service
import src.util.validators as validator_service


class DataCapture:
    """
    This is a class to perform mathematical operations on integers.
    """

    def __init__(self) -> None:
        """
        The constructor for DataCapture class.
        """

        self.data: list[int] = []

    def add(self, number) -> None:
        """
        The function to add a number to the data list.

        Parameters:
            number: The number to be added to the data list.

        Raises:
            Value Error (Exception): The input is not an integer or is
            negative.

        Returns:
            None
        """

        validator_service.Validator.validate_input(number)
        self.data.append(number)

    def build_stats(self) -> stat_builder_service.StatBuilder:
        """
        The function to build the stats object.

        Returns:
            StatBuilder: The stats object.
        """

        return stat_builder_service.StatBuilder(self.data)
