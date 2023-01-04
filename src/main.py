import src.data_capture.data_capture as data_capture_service
import src.stat_builder.stat_builder as stat_builder_service

capture: data_capture_service.DataCapture = data_capture_service.DataCapture()
capture.add(1)
capture.add(3)
capture.add(5)
capture.add(7)
capture.add(9)

print(f"Capture: {capture.data}")
stats: stat_builder_service.StatBuilder = capture.build_stats()

n_less_than_9: int = stats.less(9)
n_between_1_and_9: int = stats.between(1, 9)
n_greater_than_3: int = stats.greater(3)

print(f"Values less than 9: {n_less_than_9}")
print(f"Values between 1 and 9: {n_between_1_and_9}")
print(f"Values greater than 3: {n_greater_than_3}")

n_between_2_and_4: int = stats.between(2, 4)
n_greater_than_2: int = stats.greater(2)
n_less_than_10: int = stats.less(10)
n_between_1_and_1000: int = stats.between(1, 1000)

print(f"Values between 2 and 4: {n_between_2_and_4}")
print(f"Values greater than 2: {n_greater_than_2}")
print(f"Values less than 10: {n_less_than_10}")
print(f"Values between 1 and 1000: {n_between_1_and_1000}")
