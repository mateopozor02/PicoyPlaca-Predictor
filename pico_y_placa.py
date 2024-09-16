class Car:
    def __init__(self, license_plate):
        self._license_plate = license_plate

    def set_license_plate(self, license_plate):
        self._license_plate = license_plate

    def get_license_plate(self):
        return self._license_plate
    
    def get_last_digit(self):
        return self._license_plate[-1]