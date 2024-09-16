import unittest
from pico_y_placa import PicoYPlaca, Car 

class TestPicoYPlaca(unittest.TestCase):

    def setUp(self):
        self.pico_y_placa = PicoYPlaca()

    # Test case for restricted vehicle 
    def test_license_plate_restricted(self):
        car = Car('PBA-1231') # Car is restricted on Monday
        date = '2024-09-16' # Monday
        time = '08:00' # Time is within the restriction hours
        self.assertTrue(self.pico_y_placa.is_restricted(car, date, time))

    # Test case for unrestricted vehicle
    def test_license_plate_unrestricted(self):
        car = Car('PBA-1237') # Car is not restricted on Monday
        date = '2024-09-23' # Monday
        time = '08:00' # Time is within the restriction hours
        self.assertFalse(self.pico_y_placa.is_restricted(car, date, time))

    # Test case for not restricted day
    def test_not_restricted_day(self):
        car = Car('PBA-1231') # Car is not restricted on Sunday
        date = '2024-09-15' # Sunday
        time = '08:00' # Time is within the restriction hours
        self.assertFalse(self.pico_y_placa.is_restricted(car, date, time))

    # Test case for not restricted time
    def test_not_restricted_time(self):
        car = Car('PBA-1238') # Car is not restricted on Monday
        date = '2024-09-16' # Monday
        time = '10:00' # Time is not within the restriction hours
        self.assertFalse(self.pico_y_placa.is_restricted(car, date, time))

    # Test case for boundary times
    def test_boundary_times(self):
        car = Car('PBA-1231') # Car is not restricted on Monday
        date = '2024-09-16' # Monday
        time = '09:30' # Time is the last minute of the restriction hours
        self.assertTrue(self.pico_y_placa.is_restricted(car, date, time))

        time = '16:00' # Time is the first minute of the restriction hours
        self.assertTrue(self.pico_y_placa.is_restricted(car, date, time))