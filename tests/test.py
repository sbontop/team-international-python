from src.util import exceptions as exceptions_service

from .base import BaseTestDataCapture, BaseTestStatBuilder


class TestAddDataCapture(BaseTestDataCapture):
    def setUp(self) -> None:
        return super().setUp()

    def test_add_should_be_equal(self) -> None:
        expected: list[int] = [1, 2, 3, 4, 5]
        self.assertEqual(self.capture.data, expected)

    def test_add_should_not_be_equal_(self) -> None:
        expected: list[int] = [1, 2]
        self.assertNotEqual(self.capture.data, expected)

    def test_add_not_an_integer_should_fail(self) -> None:
        with self.assertRaises(ValueError):
            value: str = "a"
            self.capture.add(value)

    def test_add_negative_number_should_fail(self) -> None:
        with self.assertRaises(ValueError):
            value: int = -1
            self.capture.add(value)


class TestLessStatBuilder(BaseTestStatBuilder):
    def setUp(self) -> None:
        return super().setUp()

    def test_less_should_be_equal(self) -> None:
        number: int = 4
        expected: int = 3
        self.assertEqual(self.stats.less(number), expected)

    def test_less_should_not_be_equal(self) -> None:
        number: int = 4
        expected: int = 4
        self.assertNotEqual(self.stats.less(number), expected)

    def test_invalid_input_that_exceeds_max_value_should_fail(self) -> None:
        return super().test_invalid_input_that_exceeds_max_value_should_fail()


class TestBewteenStatBuilder(BaseTestStatBuilder):
    def setUp(self) -> None:
        return super().setUp()

    def test_between_should_be_equal(self) -> None:
        n1: int = 2
        n2: int = 4
        expected: int = 1
        self.assertEqual(self.stats.between(n1, n2), expected)

    def test_between_should_not_be_equal(self) -> None:
        n1: int = 2
        n2: int = 4
        expected: int = 2
        self.assertNotEqual(self.stats.between(n1, n2), expected)

    def test_between_valid_ranges_should_succeed(self) -> None:
        n1: int = 2
        n2: int = 4
        self.assertGreater(n2, n1)

    def test_between_invalid_ranges_should_fail(self) -> None:
        n1: int = 4
        n2: int = 2
        with self.assertRaises(exceptions_service.InvalidRangeGreaterError):
            self.stats.between(n1, n2)

    def test_between_range_that_is_greater_at_least_by_one_should_fail(self) -> None:
        n1: int = 1
        n2: int = 2
        with self.assertRaises(exceptions_service.InvalidRangeGreaterAtLeastByOneError):
            self.stats.between(n1, n2)


class TestGreaterStatBuilder(BaseTestStatBuilder):
    def setUp(self) -> None:
        return super().setUp()

    def test_greater_should_be_equal(self) -> None:
        number: int = 3
        expected: int = 2
        self.assertEqual(self.stats.greater(number), expected)

    def test_greater_should_not_be_equal(self) -> None:
        number: int = 3
        expected: int = 1
        self.assertNotEqual(self.stats.greater(number), expected)

    def test_invalid_input_that_exceeds_max_value_should_fail(self) -> None:
        return super().test_invalid_input_that_exceeds_max_value_should_fail()
