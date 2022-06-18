import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):

    def test_nubbin_battery_return_true(self):
        current = date.today()
        last_service_date = current.replace(year=current.year - 5)
        self.assertTrue(NubbinBattery(current, last_service_date).needs_service())

    def test_nubbin_battery_return_false(self):
        current = date.today()
        last_service_date = current.replace(year=current.year - 3)
        self.assertFalse(NubbinBattery(current, last_service_date).needs_service())
