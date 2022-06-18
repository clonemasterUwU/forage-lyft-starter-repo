import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_return_true(self):
        self.assertTrue(CapuletEngine(30003, 0).needs_service())

    def test_needs_service_return_false(self):
        self.assertFalse(CapuletEngine(30000, 0).needs_service())
