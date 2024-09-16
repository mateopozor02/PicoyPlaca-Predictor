import re

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