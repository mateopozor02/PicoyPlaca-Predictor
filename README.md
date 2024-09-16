# PicoyPlaca-Predictor

The repository cantains a Python application that predicts if a car is allowed to circulate in Quito-Ecuador
according to the city's "Pico y Placa" reglulations. These restrictions apply from Monday to Friday from 
7:00am - 9:30am in the morning, and 4:00pm - 7:30 pm in the evening. 

## Module: pico_y_placa 
This module contains the main logic behind the application. It includes two classes: Car class and PicoYPlaca class
used to represent and handle the restrictions. 

### Car Class 
It is used to represent a car object with its license plate. 
#### Methods
- `__init__(license_plate: str)`: Initializes the Car object with a given license plate. Validates the format with a setter method.
- `set_license_plate(license_plate: str)`: Sets the license plate of the car and validates the format with a regular expression. The format should be in the form ABC-1234.
- `get_license_plate() -> str`: Getter method. Returns the car's license plate.
- `get_last_digit() -> int`: Returns the last digit of the car's license plate. This is used to determine the restriction.
- `__str__() -> str`: To string method used to represent the car as it license plate.

### PicoYPlaca Class
This class is used to handle the "Pico y Placa" restrictions and the main logic to determine whether a car circulates or not. 
#### Attributes: 
- `restriction_schedule`: A dictionary mapping representing the five days of the week (0 for Monday, 4 for Friday) and the pairs of
  license plate digits with restrictions.
- `restriction_hours`: A list of tuples, each defining a time range during which restrictions are applied. These use the datetime.time() objects to
  determine restrictions easily.
#### Methods 
- `__init__()`: Initializes the instance variables needed to determine the restrictions.
- `is_restricted(car: Car, date: str, time: str) -> bool`: Checks if the given car is restricted based on its license plate, given date (YYYY-MM-DD), and time (HH:MM).
   Returns True if the car is restricted and False otherwise.

## Module: test_pico_y_placa
This module contains unit tests for the `PicoYPlaca` class, which checks if a vehicle is restricted based on its license plate, date, and time. 
The tests are written using the `unittest` framework and ensure the correct functionality of the PicoYPlaca predictor.

### Tests Included
- **Restricted vehicle**: Verifies that a vehicle with a restricted license plate is correctly identified as restricted during restricted hours on a restricted day.
- **Unrestricted vehicle**: Checks that a vehicle with a non-restricted license plate is allowed to circulate during restricted hours on a restricted day.
- **Not restricted day**:  Ensures that no vehicle is restricted on a non-restricted day (e.g., Sunday).
- **Not restricted time**:  Verifies that a vehicle is not restricted outside the defined restriction hours.
- **Boundary times**:  Tests the edge cases where the vehicle is checked at the exact start or end of the restriction hours.
