import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_return_true(self):
        self.assertTrue(CarriganTire([0.9, 0, 0, 0]).needs_service())
        self.assertTrue(CarriganTire([0, 0.9, 0, 0]).needs_service())
        self.assertTrue(CarriganTire([0, 0.9, 1, 0]).needs_service())

    def test_needs_service_return_false(self):
        self.assertFalse(CarriganTire([0, 0, 0, 0]).needs_service())
        self.assertFalse(CarriganTire([0.5, 0.6, 0.7, 0.8]).needs_service())
