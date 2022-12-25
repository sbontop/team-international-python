import unittest
from src.data_capture import DataCapture


class BaseTestDataCapture(unittest.TestCase):
    def setUp(self) -> None:
        self.capture = self.create_capture()

    def create_capture(self) -> DataCapture:
        capture: DataCapture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(3)
        capture.add(4)
        capture.add(5)
        return capture


class BaseTestStatBuilder(BaseTestDataCapture):
    def setUp(self) -> None:
        super().setUp()
        self.stats = self.capture.build_stats()
