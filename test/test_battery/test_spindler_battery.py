import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_return_true(self):
        current = date.today()
        last_service_date = current.replace(year=current.year - 3)
        self.assertTrue(SpindlerBattery(current, last_service_date).needs_service())

    def test_spindler_battery_return_false(self):
        current = date.today()
        last_service_date = current.replace(year=current.year - 1)
        self.assertFalse(SpindlerBattery(current, last_service_date).needs_service())
