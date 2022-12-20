class DataCapture():
    def __init__(self) -> None:
        self.data = []
    
    def validate(self, number) -> None:
        if not isinstance(number, int):
            raise ValueError('Only integers are allowed')
        if number < 0:
            raise ValueError('Only positive integers are allowed')

    def add(self, number) -> None:
        self.validate(number)
        self.data.append(number)

    def less(self, number) -> int:
        return len([x for x in self.data if x < number])
    
    def between(self, number1, number2) -> int:
        return len([x for x in self.data if x >= number1 and x <= number2])
    
    def greater(self, number) -> int:
        return len([x for x in self.data if x > number])
    
    def build_stats(self) -> dict:
        return {
            'min': min(self.data),
            'max': max(self.data),
            'avg': sum(self.data) / len(self.data),
            'sum': sum(self.data)
        }

if __name__ == '__main__':
    data_capture = DataCapture()
    data_capture.add(1)
    data_capture.add(2)
    data_capture.add(3)
    data_capture.add(4)
    data_capture.add(5)
    print(f"Data Capture: {data_capture.data}")
    print(f"Values less than 4: {data_capture.less(4)}")
    print(f"Values between 2 and 4: {data_capture.between(2, 4)}")
    print(f"Values greater than 3: {data_capture.greater(3)}")
    print(f"Data Capture stats: {data_capture.build_stats()}")
