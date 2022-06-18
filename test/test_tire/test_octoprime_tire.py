import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_return_true(self):
        self.assertTrue(OctoprimeTire([0.9, 0.9, 0.9, 0.9]).needs_service())
        self.assertTrue(OctoprimeTire([1, 1, 1, 0]).needs_service())

    def test_needs_service_return_false(self):
        self.assertFalse(OctoprimeTire([1, 1, 0, 0]).needs_service())
        self.assertFalse(OctoprimeTire([0.5, 0.6, 0.7, 0.8]).needs_service())
