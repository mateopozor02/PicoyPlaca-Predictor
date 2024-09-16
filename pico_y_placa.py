import re
import datetime

class Car:
    def __init__(self, license_plate):
        self._license_plate = self.set_license_plate(license_plate)

    def set_license_plate(self, license_plate):
        # Validate license plate format to be like 'PBX-1234'
        if not re.match(r'^[A-Z]{3}-\d{4}$', license_plate):
            raise ValueError('Invalid license plate format. Must be like "PBX-1234"')
        
        self._license_plate = license_plate

    def get_license_plate(self):
        return self._license_plate
    
    def get_last_digit(self):
        return self._license_plate[-1]
    
    def __str__(self):
        return f'Car with license plate {self._license_plate}'
    
class PicoYPlaca: 
    def __init__(self):
        # Define the restriction days and plate numbers
        self.restriction_schedule = {
            0: [1, 2], # Monday
            1: [3, 4], # Tuesday
            2: [5, 6], # Wednesday 
            3: [7, 8], # Thursday
            4: [9, 0] # Friday
        }

        # Define the restriction hours
        self.restriction_hours = [
            (datetime.strptime('06:00', '%H:%M'), datetime.strptime('09:00', '%H:%M')),
            (datetime.strptime('16:00', '%H:%M'), datetime.strptime('20:00', '%H:%M'))
        ]