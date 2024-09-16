import unittest
from pico_y_placa import PicoYPlaca, Car 

class TestPicoYPlaca(unittest.TestCase):
    
    def setUp(self):
        self.pico_y_placa = PicoYPlaca()