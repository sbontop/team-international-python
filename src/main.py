import src.data_capture.data_capture as data_capture_service
import src.stat_builder.stat_builder as stat_builder_service

capture = data_capture_service.DataCapture()
capture.add(1)
capture.add(2)
capture.add(3)
capture.add(4)
capture.add(5)
print(f"Capture: {capture.data}")
stats: stat_builder_service.StatBuilder = capture.build_stats()
print(f"Values less than 4: {stats.less(4)}")
print(f"Values between 2 and 4: {stats.between(2, 4)}")
print(f"Values greater than 3: {stats.greater(3)}")
